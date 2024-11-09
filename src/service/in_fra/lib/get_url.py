def get_url(*, prefecture, page):
    """
    in-fraのURLを取得

    prefectoresは1~47の整数 + その他（100）
    pageは1~の整数
    """
    return (
        f"https://www.in-fra.jp/long-internships/prefectures/{prefecture}?page={page}"
    )


