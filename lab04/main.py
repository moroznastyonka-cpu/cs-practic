import sys
from stats import average_by_city, read_valid, warmest_city, parse_record


def main():
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

    skipped = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            skipped += 1

    averages = average_by_city(records)
    best = warmest_city(records)

    print(len(records))
    print(skipped)
    print(f"{averages[best]:.1f}")


if __name__ == "__main__":
    main()