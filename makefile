run-app:
	python ./src/main.py

run-tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

