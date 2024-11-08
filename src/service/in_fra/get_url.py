def get_url(*, prefectures, page):
    """
    in-fraのURLを取得

    prefectoresは1~47の整数 + その他（100）
    pageは1~の整数
    """
    return (
        f"https://www.in-fra.jp/long-internships/prefectures/{prefectures}?page={page}"
    )


prefectures = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    100,  # その他
]
