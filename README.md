**Парсинг. Python.**
=========================

Парсер для документации Python и извлечения информации о последних версиях, статьях "Что нового", загрузке документации и статусах PEP (Python Enhancement Proposal).

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
* CSV

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
usage: main.py [-h] [-c] [-o {pretty,file}]
               {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
**Автор**
--------

[Антон Стремоусов](https://github.com/stremousoff)