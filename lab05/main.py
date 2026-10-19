from pathlib import Path

from logstats import count_levels, format_report, parse_event, top_errors


HERE = Path(__file__).parent


def main():
    filename = input().strip()
    log_path = HERE / filename

    total = 0
    error_count = 0
    broken_count = 0

    with open(log_path, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue

            total += 1

            try:
                event = parse_event(line)
            except ValueError:
                broken_count += 1
                continue

            if event["level"] == "ERROR":
                error_count += 1

    print(total)
    print(error_count)
    print(broken_count)

    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    with open(HERE / "report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report)


if __name__ == "__main__":
    main()