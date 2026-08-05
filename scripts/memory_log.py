#!/usr/bin/env python3
"""Bounded reads and lossless archival for the bot's Markdown memory logs."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_MAX_BYTES = 24_000
DEFAULT_KEEP_DAYS = 5


@dataclass(frozen=True)
class Entry:
    text: str
    date: dt.date | None


def entry_pattern(path: Path) -> re.Pattern[str]:
    name = path.name
    if name == "TRADE-LOG.md":
        return re.compile(
            r"(?m)^(?=#{2,3} (?:Day 0\b|\d{4}-\d{2}-\d{2}\b|"
            r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}\b))"
        )
    if name == "RESEARCH-LOG.md":
        return re.compile(r"(?m)^(?=## \d{4}-\d{2}-\d{2}\b)")
    if name == "WEEKLY-REVIEW.md":
        return re.compile(r"(?m)^(?=## Week ending \d{4}-\d{2}-\d{2}\b)")
    if name == "REBALANCE-LOG.md":
        return re.compile(r"(?m)^(?=## \d{4}-\d{2}-\d{2}\b)")
    raise ValueError(f"unsupported memory log: {path}")


def entry_date(text: str, fallback_year: int) -> dt.date | None:
    iso = re.match(r"#{2,3} (?:Week ending )?(\d{4}-\d{2}-\d{2})\b", text)
    if iso:
        return dt.date.fromisoformat(iso.group(1))
    short = re.match(
        r"#{2,3} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2})\b",
        text,
    )
    if short:
        month = dt.datetime.strptime(short.group(1), "%b").month
        return dt.date(fallback_year, month, int(short.group(2)))
    return None


def parse_text(path: Path, text: str, today: dt.date | None = None) -> tuple[str, list[Entry]]:
    starts = [match.start() for match in entry_pattern(path).finditer(text)]
    if not starts:
        return text, []
    fallback_year = (today or dt.date.today()).year
    preamble = text[: starts[0]]
    entries = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(text)
        entry_text = text[start:end]
        entries.append(Entry(entry_text, entry_date(entry_text, fallback_year)))
    return preamble, entries


def parse_log(path: Path, today: dt.date | None = None) -> tuple[str, list[Entry]]:
    return parse_text(path, path.read_text(encoding="utf-8"), today)


def archived_entries(path: Path, years: set[int]) -> list[Entry]:
    entries: list[Entry] = []
    for year in sorted(years):
        archive = path.parent / "archive" / f"{path.stem}-{year}.md"
        if archive.exists():
            _, parsed = parse_text(path, archive.read_text(encoding="utf-8"), dt.date(year, 12, 31))
            entries.extend(parsed)
    return entries


def utf8_size(text: str) -> int:
    return len(text.encode("utf-8"))


def day_groups(entries: list[Entry]) -> list[list[Entry]]:
    """Group adjacent entries by date without ever combining undated entries."""
    groups: list[list[Entry]] = []
    for entry in entries:
        if groups and entry.date is not None and groups[-1][0].date == entry.date:
            groups[-1].append(entry)
        else:
            groups.append([entry])
    return groups


def recent_days(entries: list[Entry], days: int) -> list[Entry]:
    groups = day_groups(entries)
    return [entry for group in groups[-days:] for entry in group]


def bounded_text(preamble: str, entries: list[Entry], max_bytes: int) -> str:
    notice = "<!-- Older entries are in memory/archive/. -->\n\n"
    base = preamble + notice
    groups = day_groups(entries)
    while len(groups) > 1:
        output = base + "".join(entry.text for group in groups for entry in group)
        if utf8_size(output) <= max_bytes:
            return output
        groups.pop(0)
    # The newest complete day is indivisible and always retained, so a single
    # unusually large day may exceed the soft byte ceiling.
    return base + "".join(entry.text for group in groups for entry in group)


def archive_header(source: Path, year: int) -> str:
    return (
        f"# Archived {source.stem.replace('-', ' ').title()} — {year}\n\n"
        f"Cold history rotated losslessly from `{source.as_posix()}`. "
        "Routine reads must use `scripts/memory_log.py`; this file is for audit lookup.\n\n"
    )


def archive_log(path: Path, keep_days: int, max_bytes: int) -> list[Path]:
    preamble, entries = parse_log(path)
    groups = day_groups(entries)
    move_groups = max(0, len(groups) - keep_days)
    while move_groups < len(groups) - 1:
        hot = preamble + "".join(
            entry.text for group in groups[move_groups:] for entry in group
        )
        if utf8_size(hot) <= max_bytes:
            break
        move_groups += 1
    if move_groups == 0:
        return []

    moved = [entry for group in groups[:move_groups] for entry in group]
    retained = [entry for group in groups[move_groups:] for entry in group]
    archive_dir = path.parent / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    changed: list[Path] = []
    by_year: dict[int, list[str]] = {}
    fallback_year = dt.date.today().year
    for entry in moved:
        year = entry.date.year if entry.date else fallback_year
        by_year.setdefault(year, []).append(entry.text)

    for year, texts in by_year.items():
        archive = archive_dir / f"{path.stem}-{year}.md"
        existing = archive.read_text(encoding="utf-8") if archive.exists() else archive_header(path, year)
        if existing and not existing.endswith("\n"):
            existing += "\n"
        archive.write_text(existing + "".join(texts), encoding="utf-8")
        changed.append(archive)

    path.write_text(preamble + "".join(entry.text for entry in retained), encoding="utf-8")
    return [path, *changed]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("recent", "week"):
        sub = subparsers.add_parser(command)
        sub.add_argument("log", type=Path)
        sub.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
        if command == "recent":
            sub.add_argument("--days", type=int, default=DEFAULT_KEEP_DAYS)

    archive = subparsers.add_parser("archive")
    archive.add_argument("log", type=Path)
    archive.add_argument("--keep-days", type=int, default=DEFAULT_KEEP_DAYS)
    archive.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.max_bytes <= 0:
        raise SystemExit("--max-bytes must be positive")
    if args.command == "archive":
        if args.keep_days < 1:
            raise SystemExit("--keep-days must be at least 1")
        for changed in archive_log(args.log, args.keep_days, args.max_bytes):
            print(changed.as_posix())
        return 0

    preamble, entries = parse_log(args.log)
    if args.command == "recent":
        if args.days < 1:
            raise SystemExit("--days must be at least 1")
        selected = recent_days(entries, args.days)
    else:
        today = dt.date.today()
        monday = today - dt.timedelta(days=today.weekday())
        entries = archived_entries(args.log, {monday.year, today.year}) + entries
        selected = [entry for entry in entries if entry.date and monday <= entry.date <= today]
    sys.stdout.write(bounded_text(preamble, selected, args.max_bytes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
