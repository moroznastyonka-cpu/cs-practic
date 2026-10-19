def parse_event(line):
    parts = line.strip().split(" | ", 2)

    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    timestamp, level, message = parts

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

    if level not in valid_levels:
        raise ValueError("Неизвестный уровень")

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
    }


def count_levels(lines):
    counts = {
        "DEBUG": 0,
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "BROKEN": 0,
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