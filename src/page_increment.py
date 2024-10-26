from urllib.parse import urlparse, parse_qs, urlunparse, urlencode


def page_increment(*, url):
    """
    urlのpageをインクリメント
    """

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if query_params.get("page") is None:
        return ""

    current_page = query_params.get("page")[0]

    query_params["page"] = int(current_page) + 1

    new_query_string = urlencode(query_params, doseq=True)
    new_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            "",
            new_query_string,
            "",
        )
    )

    return new_url
