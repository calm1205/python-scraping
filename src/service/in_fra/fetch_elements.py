from src.service.in_fra.get_url import get_url
from src.lib.fetch_soup import fetch_soup

HREF_SELECTOR = ".js-send-imp-event"
NO_HIT_SELECTOR = ".no-public-interns-alert"


def fetch_elements(*, prefecture, page):
    """
    fetchしたsoupから要素を取得
    """

    url = get_url(prefecture=prefecture, page=page)

    beautiful_soup = fetch_soup(url)
    if not beautiful_soup:  # 404 error
        print("\t\t404 page not found.")
        return None

    no_match = beautiful_soup.select(NO_HIT_SELECTOR)
    # 条件に一致する募集が見つかりませんでした。検索条件を変更して再度検索をお試しください。
    # 以降は募集が終了した企業のカードが続く。
    # if no_match:
    #     print("\t\tNo match result.")
    #     return None

    elements = beautiful_soup.select(HREF_SELECTOR)

    if not elements:  # 検索結果のカードdomが画面上に存在しない
        print("\t\tNo match card.")
        return None

    return elements
