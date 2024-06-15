run-app:
	python3 main.py

tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

pipeline: lint tests
