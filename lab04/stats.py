def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Не три поля")

    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("Пустой город или дата")

    temp = temp.replace(",", ".")

    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура не число")

    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


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
    best = ""
    for city in averages:
        if best == "" or averages[city] > averages[best]:
            best = city
        elif averages[city] == averages[best] and city < best:
            best = city
    return best