poetry build
poetry publish --dry-run
python3 -m pip install --user dist/*.whl
poetry run brain-games
