run-app:
	python3 main.py

run-tests:
	pytest

lint:
	pylint $$(git ls-files '*.py')

pipeline: lint run-tests

git-prune:
	git fetch -p