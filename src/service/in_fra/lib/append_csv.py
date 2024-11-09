from src.lib.csv.csv_format import get_csv_row
from src.lib.csv.append_csv_rows import append_csv_rows

CSV_PATH = f"/app/csv/in-fra.csv"
AFTER_RECOMMEND_CLASS = "promote-remote-intern"
HIT_CLASS = "js-card-link"


def append_csv(*, element):
    """
    csvへ追記
    """

    exist_after_recommend = AFTER_RECOMMEND_CLASS in element.get("class", [])
    # 以降のカードが検索条件に合致するものではない。
    # 青森県のように検索結果が少ない場合に検索条件に合致しない推薦カードが表示される。
    # if exist_after_recommend:
    #     print("\t\tAfter this card is recommends.")
    #     return False

    if HIT_CLASS in element.get("class", []):
        text = element.find(class_="company-name").get_text().strip()
        print(f"\t\t{text}")
        rows = [get_csv_row(text=text, link=element.get("href"))]
        append_csv_rows(rows=rows, csv_path=CSV_PATH)

    return True
