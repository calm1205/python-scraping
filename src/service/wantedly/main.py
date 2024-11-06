import time
import csv

from src.lib.project_dir import project_dir
from src.lib.csv.create_csv_only_header import create_csv_only_header
from src.lib.csv.csv_format import get_csv_row
from src.lib.csv.append_csv_rows import append_csv_rows
from src.lib.fetch_selector import fetch_selector
from src.service.wantedly.get_url import get_url, areas, occupation_types


CSV_PATH = f"/app/csv/output.csv"
HREF_SELECTOR = ".fresnel-greaterThanOrEqual-laptop .ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10"
PAGE_LIMIT = 10

create_csv_only_header(output_path=CSV_PATH)

print("fetching...")
start_time = time.time()

for area in areas:
    print(f"area: {area}")

    for occupation_type in occupation_types:
        print(f"\toccupation_type: {occupation_type}")

        for index in range(1, PAGE_LIMIT):
            print(f"\t\tpage {index}", end=" ")

            url = get_url(page=index, areas=area, occupation_types=occupation_type)

            try:
                bs_elements = fetch_selector(url=url, selector=HREF_SELECTOR)

                rows = [
                    get_csv_row(text=element.text, link=element.get("href"))
                    for element in bs_elements
                ]

                if not rows:
                    print("no more data")
                    break

                append_csv_rows(rows=rows, csv_path=CSV_PATH)
                print(f"(total: {int(time.time() - start_time)}\tsec)")
            except Exception as e:
                print(f"failed ({e})")


print("fetch done")
