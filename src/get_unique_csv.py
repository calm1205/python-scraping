import csv

from get_unique_dict_array import get_unique_dict_array


def get_unique_csv():
    """csvの重複を削除"""

    lines = []
    with open("csv/output.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lines.append(row)

    unique_lines = get_unique_dict_array(dict_array=lines)

    with open("csv/unique_output.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = unique_lines[0].keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()

        writer.writerows(unique_lines)


get_unique_csv()
