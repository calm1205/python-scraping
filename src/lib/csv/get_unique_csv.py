import csv

from src.lib.get_unique_dict_array import get_unique_dict_array
from lib.unique_by_text import unique_by_text

TARGET_CSV = "csv/in-fra.csv"
OUTPUT_CSV = "csv/unique_output.csv"


def get_unique_csv(target_csv=TARGET_CSV, output_csv=OUTPUT_CSV):
    """csvの重複を削除"""

    print("get_unique_csv")
    lines = []
    with open(target_csv, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lines.append(row)

    unique_lines = unique_by_text(dict_array=lines)

    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = unique_lines[0].keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()

        writer.writerows(unique_lines)


get_unique_csv()
