install:
	uv sync

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

check:
	make lint

.PHONY: install lint test check