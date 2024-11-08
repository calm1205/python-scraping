from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def fetch_soup(url):
    """
    fetchしたレスポンスからsoupを取得
    404エラーなどが発生した場合はNoneを返す
    """
    soup = None
    try:
        with urlopen(url) as response:
            soup = BeautifulSoup(response, "html.parser")
    except HTTPError as e:
        print(e)
    finally:
        return soup
