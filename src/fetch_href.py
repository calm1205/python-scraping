from urllib.request import urlopen
from bs4 import BeautifulSoup


def fetch_href(*, url, href_class):
    """
    fetchしたレスポンスからhref要素のテキストとhref属性を取得
    """

    results = []
    with urlopen(url) as response:
        soup = BeautifulSoup(response, "html.parser")
        elements = soup.find_all("a", class_=href_class)

        for element in elements:
            results.append({"会社名": element.text, "リンク": element.get("href")})

    return results
