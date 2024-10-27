import time
import csv

from fetch_href import fetch_href
from get_url import get_url


HREF_SELECTOR = ".fresnel-greaterThanOrEqual-laptop .ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10"
PAGE_LIMIT = 2162
PAGE_LIMIT = 100


print("fetching...")
start_time = time.time()

for index in range(1, PAGE_LIMIT):
    print(f"page {index}", end=" ")

    href_dists = fetch_href(url=get_url(page=index), href_selector=HREF_SELECTOR)

    for href_dist in href_dists:
        with open("csv/output.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(href_dist)

    print(f"done(total: {int(time.time() - start_time)} sec)")

print("fetch done")
