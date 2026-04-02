install:
	uv sync

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

.PHONY: install lint test