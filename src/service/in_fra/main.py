from src.service.in_fra.get_url import prefectures, get_url
from src.lib.fetch_selector import fetch_selector
from src.service.in_fra.fetch_soup import fetch_soup

print("hello in-fra")

HREF_SELECTOR = "intern_detail_preview"
NO_HIT_SELECTOR = "no-public-interns-alert"
PAGE_LIMIT = 217

print("fetching...")

for prefecture in prefectures:
    for page in range(1, PAGE_LIMIT):
        print(f"\tpage {page}", end=" ")
        url = get_url(prefecture=prefecture)

        beautiful_soup = fetch_soup(url)

        rows = [
            get_csv_row(text=element.text, link=element.get("href"))
            for element in bs_elements
        ]

        if not rows:
            print("no more data")
            break
        print(f"prefecture: {prefecture}")

print("fetch done")
