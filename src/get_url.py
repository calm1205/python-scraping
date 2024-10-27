# ENDPOINT = "https://dummyjson.com/test"
# ENDPOINT = "https://example.com/"


def get_url(*, page):
    return f"https://www.wantedly.com/projects?new=true&page={page}&hiringTypes=internship&hiringTypes=part_time&order=mixed"
