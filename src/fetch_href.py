from urllib.request import urlopen
from bs4 import BeautifulSoup


def fetch_href(*, url: str, href_class: str):
    """
    fetchしたレスポンスからhref要素のテキストとhref属性を取得
    """

    results = []
    with urlopen(ENDPOINT) as response:
        soup = BeautifulSoup(response, "html.parser")
        elements = soup.find_all("a", class_=HREF_CLASS)

        for element in elements:
            results.append({"text": element.text, "href": element.get("href")})

    return results
