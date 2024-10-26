from urllib.request import urlopen
from bs4 import BeautifulSoup

ENDPOINT = 'https://dummyjson.com/test' # dummy data
ENDPOINT = 'https://www.wantedly.com/projects?new=true&page=1&hiringTypes=internship&hiringTypes=part_time&order=mixed'

HREF_CLASS = 'ProjectListJobPostItem__CompanyLink-sc-bjcnhh-10 oYEY'

with urlopen(ENDPOINT) as response:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1").text
    print(title)
    for line in response:
        line = line.decode('utf-8')
        if HREF_CLASS in line:
            print('hit')