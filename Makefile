install:
	uv cache clean && uv tool install . --force

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

check:
	make lint

.PHONY: install lint test test-coverage check