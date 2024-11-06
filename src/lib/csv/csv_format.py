csv_interface = {"text": "str", "link": "str"}


def get_csv_row(*, text, link):
    """csvの行に整形"""
    return {"text": text, "link": link}
