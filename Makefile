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
	python3 -m pip install --user dist/*.whl --force-reinstall

# для запуска через make
brain-games:
	poetry run brain-games
