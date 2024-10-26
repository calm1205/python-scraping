from fetch_href import fetch_href


ENDPOINT = "https://dummyjson.com/test"  # dummy data
ENDPOINT = "https://www.wantedly.com/projects?new=true&page=1&hiringTypes=internship&hiringTypes=part_time&order=mixed"

HREF_CLASS = "ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10 oYEY"

print(fetch_href(url=ENDPOINT, href_class=HREF_CLASS))
