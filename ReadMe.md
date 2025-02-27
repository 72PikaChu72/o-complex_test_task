# Прогноз погоды в веб-приложении

Простое веб-приложение, позволяющее пользователям получить прогноз погоды для введенного города.

## Функции

* Ввести имя города, чтобы получить текущий прогноз погоды
* Получить информацию о температуре, скорости ветра и других параметрах погоды
* Данные получены с помощью [open-meteo.com](https://open-meteo.com/)
* Статистика запросов хранится в локальном базе данных SQLite и может быть просмотрена на странице `/stats`

## Технологии

1. [Sanic](https://sanicframework.org/) 
Асинхронный фреймворк и веб-сервер для создания веб-приложений на Python.
2. [Jinja2](https://jinja.palletsprojects.com/)
Шаблонизатор для создания веб-страниц.
3. [SQLite](https://www.sqlite.org/)
База данных SQLite.
## Как запустить

1. Установите необходимые пакеты с помощью `pip install -r requirements.txt`
2. Запустите приложение с помощью `python main.py`
3. Откройте веб-страницу по адресу [http://localhost:3000](http://localhost:3000)

## Как протестировать

1. Запустите тесты с помощью `pytest tests.py`

## Примечания

1. Приложение тестировалось и разрабатывалось на python 3.12.3

2. Прогноз погоды и предыдущий ввод пользователя выводятся с помощью шаблонизатора Jinja2

3. Предыдущий ввод пользователя хранится в session в cookie браузера

## Пометки для проверяющего

* Написаны тесты
* Cделаны автодополнение (подсказки) при вводе города
* При повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
* Статистика сохраняется для каждого города, не пользователя и её можно просмотреть используя `/stats`
* Задание выполнено в формате Proof of Concept буквально за пару часов

