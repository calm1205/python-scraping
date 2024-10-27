import time
import csv

from project_dir import project_dir
from export_csv_header import export_csv_header
from get_url import get_url
from fetch_selector import fetch_selector
from csv_format import get_csv_row
from append_csv_rows import append_csv_rows


CSV_PATH = f"{project_dir}/csv/output.csv"
HREF_SELECTOR = ".fresnel-greaterThanOrEqual-laptop .ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10"
PAGE_LIMIT = 100

export_csv_header(output_path=CSV_PATH)

print("fetching...")
start_time = time.time()

for index in range(1, PAGE_LIMIT):
    print(f"\tpage {index}", end=" ")

    url = get_url(page=index)
    bs_elements = fetch_selector(url=url, selector=HREF_SELECTOR)

    rows = [
        get_csv_row(text=element.text, link=element.get("href"))
        for element in bs_elements
    ]

    append_csv_rows(rows=rows, csv_path=CSV_PATH)
    print(f"done(total: {int(time.time() - start_time)}\tsec)")

print("fetch done")
