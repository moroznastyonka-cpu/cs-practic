def parse_event(line):
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    timestamp, level, message = parts

    valid_levels = {"INFO", "ERROR", "WARNING"}

    if level not in valid_levels:
        raise ValueError("Неизвестный уровень")

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
        else:
            counts[event["level"]] += 1

    return counts


def top_errors(lines, n):
    messages = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            messages[message] = messages.get(message, 0) + 1

    sorted_messages = sorted(
        messages.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return [[message, count] for message, count in sorted_messages[:n]]


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