run-app:
	python main.py

tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

pipeline: lint tests
