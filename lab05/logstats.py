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