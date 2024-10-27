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
