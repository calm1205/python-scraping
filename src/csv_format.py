csv_interface = {"text": "str", "link": "str"}


def get_csv_line(*, text, link):
    """csvの行に整形"""
    return {"text": args.text, "link": args["link"]}
