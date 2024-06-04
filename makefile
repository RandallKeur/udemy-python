run-app:
	python main.py

run-tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

