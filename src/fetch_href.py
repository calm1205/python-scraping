from urllib.request import urlopen
from bs4 import BeautifulSoup


def fetch_href(*, url, href_selector):
    """
    fetchしたレスポンスからhref要素のテキストとhref属性を取得
    """

    results = []
    with urlopen(url) as response:
        soup = BeautifulSoup(response, "html.parser")
        elements = soup.select(href_selector)

        for element in elements:
            results.append([element.text, element.get("href")])

    return results
