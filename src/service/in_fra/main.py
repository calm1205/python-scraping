from src.service.in_fra.prefectures import prefectures, prefecture_dict
from src.service.in_fra.get_url import get_url
from src.lib.csv.create_csv_only_header import create_csv_only_header
from src.lib.csv.csv_format import get_csv_row
from src.lib.csv.append_csv_rows import append_csv_rows
from src.lib.fetch_soup import fetch_soup

CSV_PATH = f"/app/csv/output.csv"

HREF_SELECTOR = ".js-send-imp-event"
HIT_CLASS = "js-card-link"
NO_HIT_SELECTOR = ".no-public-interns-alert"
AFTER_RECOMMEND_CLASS = "promote-remote-intern"
# PAGE_LIMIT = 217
PAGE_LIMIT = 2

create_csv_only_header(output_path=CSV_PATH)

print("fetching...")

for prefecture in prefectures:
    if prefecture == 3:
        break
    print(f"prefecture: {prefecture_dict[prefecture]}")

    for page in range(1, PAGE_LIMIT):
        print(f"\tpage {page}:")

        url = get_url(prefecture=prefecture, page=page)

        beautiful_soup = fetch_soup(url)
        if not beautiful_soup:  # 404 error
            print("\t\t404 page not found.")
            break

        no_match = beautiful_soup.select(NO_HIT_SELECTOR)
        if no_match:  # 条件に一致する結果なし
            print("\t\tNo match result.")
            break

        elements = beautiful_soup.select(HREF_SELECTOR)

        if not elements:  # 検索結果のカードdomが画面上に存在しない
            print("\t\tNo match card.")
            break

        for element in elements:
            if AFTER_RECOMMEND_CLASS in element.get(
                "class", []
            ):  # 以降のカードが検索条件に合致するものではない
                print("\t\tAfter this card is recommends.")
                break

            if HIT_CLASS in element.get("class", []):
                text = element.find(class_="company-name").get_text().strip()
                print(f"\t\t{text}")
                rows = [get_csv_row(text=text, link=element.get("href"))]
                append_csv_rows(rows=rows, csv_path=CSV_PATH)

        print("")

print("fetch done")
