.PHONY: src tests

up:
		docker compose up -d

in:
		docker compose exec app bash

run:
		docker compose exec app bash -c "python -m src.main"

run-wantedly:
		docker compose exec app bash -c "python -m src.service.wantedly.main"

run-in-fra:
		docker compose exec app bash -c "python -m src.service.in_fra.main"

test:
		docker compose exec app bash -c "make test-python"

test-auto:
		docker compose exec -T app bash -c "make test-python"

test-python:
		python -m unittest discover -s tests