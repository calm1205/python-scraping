import csv

from src.lib.fetch_selector import fetch_selector
from src.lib.csv.create_csv_only_header import create_csv_only_header
from src.lib.csv.append_csv_rows import append_csv_rows
from src.lib.csv.csv_format import get_csv_row


TARGET_CSV = "csv/in-fra.csv"
SELECTOR = ".intern-detail-desc-url a"
OUTPUT_CSV_PATH = "/app/csv/output_in-fra.csv"

create_csv_only_header(output_path=OUTPUT_CSV_PATH)

print("fetching...")


def scraping_company_url():
    """
    企業のURLを取得

    in-fra内の企業のURLから公式サイトのURLを取得してCSVに保存
    """
    with open(TARGET_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            bs_elements = fetch_selector(url=row["link"], selector=SELECTOR)
            if not bs_elements:
                continue

            link = bs_elements[0].get("href")
            name = row["text"]
            rows = [get_csv_row(text=name, link=link)]

            append_csv_rows(rows=rows, csv_path=OUTPUT_CSV_PATH)

            print(link)


scraping_company_url()
print("fetch done")
