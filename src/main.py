from fetch_href import fetch_href
from export_csv import export_csv


# ENDPOINT = "https://dummyjson.com/test"  # dummy data
HREF_CLASS = "ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10 oYEY"


def get_url(*, page):
    return f"https://www.wantedly.com/projects?new=true&page={page}&hiringTypes=internship&hiringTypes=part_time&order=mixed"


results = []

print("fetching...")
for index in range(1, 2162):
    print(f"fetching page {index}...", end=" ")
    url = get_url(page=index)
    href_dists = fetch_href(url=url, href_class=HREF_CLASS)
    results.extend(href_dists)
    print("done")

print("fetch done")

print("exporting...")
export_csv(rows=results, output_path="./csv/output.csv")
print("export done")
