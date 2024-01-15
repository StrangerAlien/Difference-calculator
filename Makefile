install:
	poetry install

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage:
	poetry run pytest --cov

lint:
	poetry run flake8 gendiff tests

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

start:	build package-install