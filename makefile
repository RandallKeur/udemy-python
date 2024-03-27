run-tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

