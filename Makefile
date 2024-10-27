.PHONY: src tests

up:
		docker compose up -d

in:
		docker compose exec app bash

run:
		docker compose exec app bash -c "python -m src.main"

test:
		docker compose exec app bash -c "make test-python"

test-python:
		python -m unittest discover -s tests
