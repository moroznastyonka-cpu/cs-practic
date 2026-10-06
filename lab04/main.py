"""Читает журнал метеостанции и печатает отчёт."""
import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    averages = average_by_city(records)
    best = warmest_city(records)

    print(len(records))
    print(0)
    print(f"{averages[best]:.1f}" if best else "0.0")


if __name__ == "__main__":
    main()
