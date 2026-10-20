def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result

