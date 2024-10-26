from urllib.request import urlopen

ENDPOINT = 'https://dummyjson.com/test' # dummy data
ENDPOINT = 'https://www.wantedly.com/projects?new=true&page=1&hiringTypes=internship&hiringTypes=part_time&order=mixed'

with urlopen(ENDPOINT) as response:
    for line in response:
        line = line.decode('utf-8')
        print(line)