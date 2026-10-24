# Лабораторная работа №6

Автоматизация тестирования веб-форм с Selenium WebDriver, POM и Allure.

## Установка
pip install -r requirements.txt

## Запуск
pytest tests/test_yandex_form.py -v
pytest tests/test_yandex_form.py -n 2 -v
pytest --alluredir=allure-results
allure serve allure-results