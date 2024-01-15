install:
		poetry install

gendiff:
		poetry run gendiff

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force-reinstall --user dist/*.whl

lint:
		poetry run flake8 gendiff

selfcheck:
		poetry check

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build