import pytest
import allure
from pages.yandex_form_page import YandexFormPage


@allure.suite("Тестирование поиска Яндекс")
class TestYandexSearch:

    @allure.title("Тест поиска и проверки результатов")
    @pytest.mark.parametrize("search_query,expected_text", [
        ("Selenium WebDriver", "Selenium"),
        ("Python автоматизация тестирования", "Python"),
        ("Тестирование программного обеспечения", "тестирование")
    ])
    def test_yandex_search_functionality(self, browser, base_url, search_query, expected_text):
        with allure.step("Открыть главную страницу Яндекс"):
            page = YandexFormPage(browser)
            page.open_page(base_url)

        with allure.step(f"Выполнить поиск: {search_query}"):
            page.perform_search(search_query)

        with allure.step("Проверить результаты"):
            first = page.get_first_result_text()
            assert first is not None, "Результаты не отобразились"
            assert expected_text.lower() in first.lower(), \
                f"Ожидаемый текст '{expected_text}' не найден в '{first}'"

    @allure.title("Тест отображения подсказок")
    def test_suggest_display(self, browser, base_url):
        page = YandexFormPage(browser)
        page.open_page(base_url)
        page.enter_search_text("автоматизация тестирования")
        page.wait_for_suggest()

    @allure.title("Тест очистки поисковой строки")
    def test_search_input_clear(self, browser, base_url):
        page = YandexFormPage(browser)
        page.open_page(base_url)
        page.enter_search_text("текст для очистки")
        el = browser.find_element(*page.SEARCH_INPUT)
        el.clear()
        assert el.get_attribute("value") == "", "Поле не очищено"