import unittest
import os

from src.export_csv import export_csv

OUTPUT_PATH = "./csv/test.csv"
test_rows = [
    {"名前": "田中", "年齢": 30, "都市": "東京"},
    {"名前": "鈴木", "年齢": 25, "都市": "大阪"},
    {"名前": "佐藤", "年齢": 22, "都市": "福岡"},
]


class TestAddFunction(unittest.TestCase):
    def tearDown(self):
        """テスト実行後に呼ばれるメソッド"""
        try:
            if os.path.exists(OUTPUT_PATH):
                os.remove(OUTPUT_PATH)
        except Exception as e:
            print(f"Error removing file {OUTPUT_PATH}: {e}")

    def test_export_csv(self):
        """csvがexportできること"""

        export_csv(rows=test_rows, output_path=OUTPUT_PATH)

        self.assertTrue(os.path.exists(OUTPUT_PATH))

    def test_csv_header(self):
        """csvにheaderが出力されること"""

        export_csv(rows=test_rows, output_path=OUTPUT_PATH)

        with open(OUTPUT_PATH, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            header = lines[0].strip()

            self.assertEqual(header, "名前,年齢,都市")


if __name__ == "__main__":
    unittest.main()
