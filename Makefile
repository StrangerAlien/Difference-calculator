.DEFAULT_GOAL := default

default:
	make build
	make publish
	make package-install

install:
	poetry install

build:
	rm -rf ./dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest