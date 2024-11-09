def unique_by_text(*, dict_array):
    """textの重複を削除"""
    unique_line = []
    seen = set()

    for item in dict_array:
        identifier = item["text"]

        if identifier not in seen:
            seen.add(identifier)
            unique_line.append(item)

    return unique_line
