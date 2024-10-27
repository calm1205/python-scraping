from urllib.request import urlopen
from bs4 import BeautifulSoup


def fetch_selector(*, url, selector):
    """
    fetchしたレスポンスからselectorを取得
    """

    with urlopen(url) as response:
        soup = BeautifulSoup(response, "html.parser")
        elements = soup.select(selector)

        return elements

        # for element in elements:
        #     results.append([element.text, element.get("href")])
