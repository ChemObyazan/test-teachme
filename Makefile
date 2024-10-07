PYTEST=pytest

ALLURE_DIR=allure-results

test_all:
	@echo ������ ���� ������
	$(PYTEST)

test_api:
	@echo ������ API ������
	$(PYTEST) tests/test_api.py

test_ui:
	@echo ������ UI ������
	$(PYTEST) tests/test_main_page.py tests/test_product_page.py tests/test_basket_page.py tests/test_favorites_page.py

test_allure:
	@echo ������ ���� ������ � ���������� Allure ������
	$(PYTEST) --alluredir=$(ALLURE_DIR)

allure_report:
	@echo ��������� Allure ������
	allure serve $(ALLURE_DIR)

clean:
	@echo ������� ����� � �������� Allure
	rm -rf $(ALLURE_DIR)