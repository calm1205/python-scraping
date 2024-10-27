def get_unique_dict_array(*, dict_array):
    """dict_arrayの重複を削除"""
    unique_line = []
    seen = set()

    for item in dict_array:
        identifier = tuple(item[key] for key in item.keys())

        if identifier not in seen:
            seen.add(identifier)
            unique_line.append(item)

    return unique_line
