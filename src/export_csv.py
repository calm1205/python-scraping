import csv


def export_csv(*, rows, output_path):
    """
    CSVファイルを出力

    e.g.
    rows = [
        {"名前": "田中", "年齢": 30, "都市": "東京"},
        {"名前": "鈴木", "年齢": 25, "都市": "大阪"},
        {"名前": "佐藤", "年齢": 22, "都市": "福岡"},
    ]
    """
    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()

        writer.writerows(rows)
