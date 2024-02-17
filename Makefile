# Установка зависимостей install
install:  
	poetry install 

# Создавание dist  с файлами для устанвки пакета
build:
	poetry build

# Отладка публикации (dry run = фикция действия)
publish:
	poetry publish --dry-run

# Установка пакета в интерпретатор python на локальном компе (мой)
package-install:
	python3 -m pip install dist/*.whl --force-reinstall

# для запуска игры через make
brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

make lint:
	poetry run flake8 brain_games
