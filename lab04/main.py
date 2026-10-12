"""Читает журнал метеостанции и печатает отчёт."""
import sys

from stats import average_by_city, parse_record, read_valid, warmest_city


def count_skipped(lines: list[str]) -> int:
    skipped = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            skipped += 1
    return skipped


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    averages = average_by_city(records)
    best = warmest_city(records)

    print(len(records))
    print(count_skipped(lines))
    print(f"{averages[best]:.1f}" if best else "0.0")


if __name__ == "__main__":
    main()