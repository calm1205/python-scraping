# python-scraping

## To run

```bash
$ make up
$ make run
```

<br/><br/>

## Setup auto test

```bash
echo '#!/bin/sh\n\nmake test-auto' > .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

<br/><br/>

## scraping target

- https://www.wantedly.com/projects?new=true&page=1&hiringTypes=internship&hiringTypes=part_time&order=mixed
- https://www.in-fra.jp/long-internship
