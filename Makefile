.PHONY: src tests

up:
		docker compose up -d && docker compose exec app bash

test:
		python -m unittest discover -s tests
