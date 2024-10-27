# ENDPOINT = "https://dummyjson.com/test"
# ENDPOINT = "https://example.com/"

areas = [
    "tokyo",
    # "osaka",
    # "nagoya",
    # "kyoto",
    # "fukuoka",
    # "tohoku",
    # "hokuriku",
    # "tokai",
    # "kinki",
    # "chugoku",
    # "kyushu",
]

occupation_types = [
    "jp__engineering",
    "jp__design_and_art",
    "jp__pm_and_web_direction",
    "jp__editing_and_writing",
    "jp__marketing",
    "jp__sales",
    "jp__customer_success_and_support",
    "jp__corporate",
    "jp__consulting",
    "jp__medical",
    "jp__others",
]


def get_url(*, page="1", areas="tokyo", occupation_types="jp__engineering"):
    return f"https://www.wantedly.com/projects?new=true&page={page}&areas={areas}&occupationTypes={occupation_types}&hiringTypes=internship&hiringTypes=part_time&order=mixed"
