install:
	poetry install

brain-games:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 gendiff tests
