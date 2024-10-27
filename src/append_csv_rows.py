import csv
from src.csv_format import csv_interface


def append_csv_rows(*, rows, csv_path):
    """CSVファイルへ追記"""

    with open(csv_path, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = csv_interface.keys()
        writer = csv.DictWriter(file, fieldnames)

        for row in rows:
            writer.writerow(row)
