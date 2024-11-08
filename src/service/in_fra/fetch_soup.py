def fetch_soup(url):
    """
    fetchしたレスポンスからsoupを取得
    """
    with urlopen(url) as response:
        soup = BeautifulSoup(response, "html.parser")
        return soup
