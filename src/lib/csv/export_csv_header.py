import csv
from src.lib.csv.csv_format import csv_interface


def export_csv_header(*, output_path):
    """CSVファイルをヘッダーのみ出力"""

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = csv_interface.keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()
