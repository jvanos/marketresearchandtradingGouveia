import datetime as dt
import tempfile
import unittest
from pathlib import Path

from scripts.memory_log import (
    archive_log,
    archived_entries,
    bounded_text,
    parse_log,
    recent_days,
    utf8_size,
)


class MemoryLogTest(unittest.TestCase):
    def write_log(self, directory: str, name: str, body: str) -> Path:
        path = Path(directory) / name
        path.write_text(body, encoding="utf-8")
        return path

    def test_trade_parser_ignores_nested_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_log(
                directory,
                "TRADE-LOG.md",
                "# Trade Log\n\n## 2026-08-01 — Buildout\n\n### Exits\nold\n\n"
                "### Aug 04 — EOD Snapshot\nnew\n",
            )
            preamble, entries = parse_log(path, dt.date(2026, 8, 4))
            self.assertEqual("# Trade Log\n\n", preamble)
            self.assertEqual(2, len(entries))
            self.assertIn("### Exits", entries[0].text)
            self.assertEqual(dt.date(2026, 8, 4), entries[1].date)

    def test_archive_is_lossless_and_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            original = "# Research Log\n\n" + "".join(
                f"## 2026-07-{day:02d} — Check\nentry {day}\n\n" for day in range(1, 5)
            )
            path = self.write_log(directory, "RESEARCH-LOG.md", original)
            changed = archive_log(path, keep_days=2, max_bytes=10_000)
            archive = Path(directory) / "archive" / "RESEARCH-LOG-2026.md"
            self.assertEqual([path, archive], changed)
            combined = archive.read_text(encoding="utf-8") + path.read_text(encoding="utf-8")
            for day in range(1, 5):
                self.assertEqual(1, combined.count(f"entry {day}"))
            self.assertEqual([], archive_log(path, keep_days=2, max_bytes=10_000))

    def test_bounded_output_honors_byte_limit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_log(
                directory,
                "WEEKLY-REVIEW.md",
                "# Weekly Review\n\n## Week ending 2026-07-25\n" + ("x" * 300) +
                "\n## Week ending 2026-08-01\n" + ("y" * 300) + "\n",
            )
            preamble, entries = parse_log(path)
            output = bounded_text(preamble, entries, 500)
            self.assertLessEqual(utf8_size(output), 500)
            self.assertIn("memory/archive/", output)
            self.assertNotIn("x" * 20, output)
            self.assertIn("y" * 20, output)

    def test_newest_day_is_never_truncated(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_log(
                directory,
                "TRADE-LOG.md",
                "# Trade Log\n\n## 2026-08-04 — Buildout\n" + ("x" * 2_000) + "\n",
            )
            preamble, entries = parse_log(path)
            output = bounded_text(preamble, entries, 500)
            self.assertGreater(utf8_size(output), 500)
            self.assertIn("x" * 2_000, output)

    def test_recent_days_keeps_all_entries_for_boundary_day(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_log(
                directory,
                "TRADE-LOG.md",
                "# Trade Log\n\n## 2026-08-01 — Buildout\nold\n\n"
                "## 2026-08-03 — Buildout\nbuy\n\n"
                "### Aug 03 — EOD Snapshot\nclose\n",
            )
            _, entries = parse_log(path, dt.date(2026, 8, 4))
            selected = recent_days(entries, 1)
            self.assertEqual(2, len(selected))
            self.assertIn("buy", selected[0].text)
            self.assertIn("close", selected[1].text)

    def test_week_can_recover_entries_rotated_to_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_log(
                directory,
                "TRADE-LOG.md",
                "# Trade Log\n\n## 2026-08-03 — Buildout\nold\n\n"
                "### Aug 04 — EOD Snapshot\nnew\n",
            )
            archive_log(path, keep_days=1, max_bytes=10_000)
            cold = archived_entries(path, {2026})
            _, hot = parse_log(path, dt.date(2026, 8, 4))
            week = [entry for entry in cold + hot if entry.date and entry.date >= dt.date(2026, 8, 3)]
            self.assertEqual(2, len(week))
            self.assertIn("old", week[0].text)
            self.assertIn("new", week[1].text)


if __name__ == "__main__":
    unittest.main()
