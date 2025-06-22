# scrapy_parser_pep

Учебный проект - парсер PEP-документации на `scrapy`.

Реализация проекта: [Сергей Баранов](https://github.com/sergei-baranov/).

Pipeline собирает текущий стейт PEP-ов на момент запуска из https://peps.python.org/.

Формирует два файла:

- `results/pep_<timestamp>.csv` - список PEP-ов в формате CSV
- `results/statuses_<timestamp>.csv` - статистика по статусам PEP-ов в формате CSV

## Установка

Создать виртуальное окружение и установить зависимости:

```bash
(venv) .../scrapy_parser_pep$ pip install -r requirements.txt
```

## Запуск

```bash
(venv) .../scrapy_parser_pep$  scrapy crawl pep
```
