build:
	poetry build

install:
	poetry install

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

make lint:
	poetry run flake8 .

make tests:
	poetry run pytest