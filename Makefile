build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 .

tests:
	poetry run pytest --cov=gendiff tests --cov-report xml
