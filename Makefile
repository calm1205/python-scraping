.PHONY: src tests

up:
		docker compose up -d && docker compose exec app bash

run:
		python -m src.main

test:
		python -m unittest discover -s tests
