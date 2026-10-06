def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("ожидалось 3 поля")

    city, temp, date = parts
    city = city.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("город или дата пустые")

    return {"city": city, "temperature": float(temp), "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    return [parse_record(line) for line in lines]


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
    return sorted(averages, key=lambda c: (-averages[c], c))[0]