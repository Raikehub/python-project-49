start:
	poetry run brain-games
install:
	poetry install
	poetry build
	python3 -m pip install dist/*.whl
lint:
	poetry run black brain_games
	poetry run flake8 brain_games