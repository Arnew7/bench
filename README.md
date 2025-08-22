# HTTP Benchmark

'Тестовое задание "Асинхронный HTTP-бенчмарк"' на Python для компании 
ИнфоТеКС
---

## Возможности

- Асинхронное выполнение HTTP GET-запросов.
- Поддержка списка хостов через аргументы или файл.
- Настройка количества запросов на каждый хост.
- Вывод отчёта: количество успешных, неудачных запросов, ошибок, минимальное/максимальное/среднее время ответа.
- Сохранение отчёта в файл.
- Unit и end-to-end тесты с поддержкой `pytest` и `pytest-asyncio`.

---

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/Arnew7/bench.git
cd bench
```
Создайте виртуальное окружение и активируйте его:
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Установите зависимости:
```
pip install --upgrade pip
pip install -r requirements.txt
```
Структура проекта:
```
bench/
├── __main__.py      # Точка входа
├── cli.py           # Парсинг аргументов и валидация
├── fetcher.py       # Асинхронные HTTP-запросы
├── models.py        # dataclass-ы для результатов
├── reporter.py      # Форматирование и вывод отчёта
└── runner.py        # Основная логика бенчмарка

tests/
├── test_cli.py
├── test_models.py
├── test_reporter.py
├── test_runner.py
└── test_e2e.py

requirements.txt
README.md
tox.ini
```
Запуск:
```
python -m bench -H https://ya.ru,https://google.com -C 5

Аргументы:
-H, --hosts — список хостов через запятую.
-F, --file — путь к файлу со списком хостов (каждый хост на новой строке, можно с комментарием через #).
-C, --count — количество запросов на каждый хост (по умолчанию 1).
-O, --output — файл для сохранения отчёта.

Пример вывода
========================================================================
Host   : https://ya.ru
Success: 5
Failed : 0
Errors : 0
Min    : 100.12 ms
Max    : 120.45 ms
Avg    : 110.23 ms
========================================================================
Host   : https://google.com
Success: 5
Failed : 0
Errors : 0
Min    : 80.11 ms
Max    : 90.99 ms
Avg    : 85.44 ms
========================================================================
Тестирование
Unit и End-to-End тесты
Тесты написаны с использованием pytest и pytest-asyncio для асинхронных функций.
Запуск тестов:

pytest --maxfail=1 --disable-warnings -q

или устанавливаем tox

python3 -m pip install tox

переходим в репозиторий и запускаем тест командой

tox

Все async def тесты обернуты в @pytest.mark.asyncio для корректного выполнения.
моков

Каждый модуль отвечает за отдельную ответственность:
cli.py — ввод и валидация.
fetcher.py — асинхронные HTTP-запросы.
runner.py — запуск и сбор результатов.
reporter.py — формирование отчёта.
models.py — структура данных.
```

Проект открыт и распространяется под лицензией MIT.
