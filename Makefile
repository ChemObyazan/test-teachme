PYTEST=pytest

ALLURE_DIR=allure-results

test_all:
	@echo Запуск всех тестов
	$(PYTEST)

test_api:
	@echo Запуск API тестов
	$(PYTEST) tests/test_api.py

test_ui:
	@echo Запуск UI тестов
	$(PYTEST) tests/test_main_page.py tests/test_product_page.py tests/test_basket_page.py tests/test_favorites_page.py

test_allure:
	@echo Запуск всех тестов с генерацией Allure отчета
	$(PYTEST) --alluredir=$(ALLURE_DIR)

allure_report:
	@echo Генерация Allure отчета
	allure serve $(ALLURE_DIR)

clean:
	@echo Очистка папки с отчетами Allure
	rm -rf $(ALLURE_DIR)