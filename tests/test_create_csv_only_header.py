import unittest
import os

from src.lib.csv.create_csv_only_header import create_csv_only_header

OUTPUT_PATH = "csv/test.csv"


class TestAddFunction(unittest.TestCase):
    def tearDown(self):
        """テスト実行後に呼ばれるメソッド"""
        try:
            if os.path.exists(OUTPUT_PATH):
                os.remove(OUTPUT_PATH)
        except Exception as e:
            print(f"Error removing file {OUTPUT_PATH}: {e}")

    def test_create_csv_only_header(self):
        """csvがexportできること"""

        create_csv_only_header(output_path=OUTPUT_PATH)

        self.assertTrue(os.path.exists(OUTPUT_PATH))

    def test_exist_csv_header(self):
        """csvにheaderが出力されること"""

        create_csv_only_header(output_path=OUTPUT_PATH)

        with open(OUTPUT_PATH, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            header = lines[0].strip()

            self.assertEqual(header, "text,link")


if __name__ == "__main__":
    unittest.main()
