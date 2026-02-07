import json
import tempfile
import unittest
from pathlib import Path

from scripts.counter import increment_counter


class CounterTests(unittest.TestCase):
    def test_increment_creates_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "counter.json"
            value = increment_counter(path)

            self.assertEqual(value, 1)
            data = json.loads(path.read_text())
            self.assertEqual(data["value"], 1)

    def test_increment_existing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "counter.json"
            path.write_text(json.dumps({"value": 2}))

            value = increment_counter(path)

            self.assertEqual(value, 3)
            data = json.loads(path.read_text())
            self.assertEqual(data["value"], 3)


if __name__ == "__main__":
    unittest.main()
