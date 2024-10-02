start:
	poetry run brain-games
install:
	poetry install
	poetry build
	python3 -m pip install dist/*.whl