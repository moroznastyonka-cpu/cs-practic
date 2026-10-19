def parse_event(line):
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Некорректная строка")

    timestamp, level, message = parts

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

    if level not in valid_levels or not message:
        raise ValueError("Некорректная строка")

    return {
        "time": timestamp,
        "level": level,
        "message": message,
    }


def count_levels(lines):
    counts = {
        "INFO": 0,
        "ERROR": 0,
        "BROKEN": 0,
        "WARNING": 0,
    }

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] += 1
            continue

        if event["level"] in counts:
            counts[event["level"]] += 1

    return counts


def top_errors(lines, limit):
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            errors[message] = errors.get(message, 0) + 1

    sorted_errors = sorted(
        errors.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return sorted_errors[:limit]


def format_report(counts, errors):
    lines = [
        "Отчёт по журналу",
        "",
    ]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.extend([
        "",
        "Частые ошибки:",
    ])

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"