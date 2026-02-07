import argparse
import json
from pathlib import Path


def increment_counter(path: Path) -> int:
    value = 0
    if path.exists():
        data = json.loads(path.read_text())
        value = int(data.get("value", 0))
    value += 1
    path.write_text(json.dumps({"value": value}))
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Increment a JSON counter.")
    parser.add_argument("--path", default="counter.json", help="Path to counter JSON.")
    args = parser.parse_args()

    value = increment_counter(Path(args.path))
    print(value)


if __name__ == "__main__":
    main()
