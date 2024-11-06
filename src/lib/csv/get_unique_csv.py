import csv

from get_unique_dict_array import get_unique_dict_array

TARGET_CSV = "csv/output.csv"
OUTPUT_CSV = "csv/unique_output.csv"


def get_unique_csv(target_csv=TARGET_CSV, output_csv=OUTPUT_CSV):
    """csvの重複を削除"""

    lines = []
    with open(target_csv, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lines.append(row)

    unique_lines = get_unique_dict_array(dict_array=lines)

    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = unique_lines[0].keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()

        writer.writerows(unique_lines)
