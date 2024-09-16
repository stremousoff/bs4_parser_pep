**Проект Парсера Python**
=========================

Парсер для парсинга документации Python и извлечения информации о последних версиях, статьях "Что нового", загрузке документации и статусах PEP (Python Enhancement Proposal).

**Возможности**
------------

* Вывод результатов в консоль в виде обычного текста
* Вывод результатов в консоль в виде таблицы PrettyTable
* Вывод результатов в файл CSV для дальнейшей обработки

**Использованные технологии**
---------------------------

* Python
* BeautifulSoup
* requests_cache
* tqdm

**Установка**
------------

1. Клонировать репозиторий и перейти в него:
```bash
git clone https://github.com/stremousoff/bs4_parser_pep.git
cd bs4_parser_pep
```
2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/scripts/activate
```
3. Установить зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
**Использование**
--------------

Запустить парсер из командной строки с желаемыми параметрами:
```bash
python src/main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}
```
**Автор**
--------

[Антон Стремоусов](https://github.com/stremousoff)