import csv
from csv_interface import csv_interface


def append_csv_rows(*, row, csv_path):
    """CSVファイルへ追記"""

    with open(csv_path, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = csv_interface.keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writerow(row)
