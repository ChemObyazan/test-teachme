PYTEST=pytest
ALLURE_DIR=allure-results

test_all:
	@echo "Running all tests"
	$(PYTEST)

test_ui:
	@echo "Running all UI tests"
	$(PYTEST) tests/test_*.py

test_api:
	@echo "Running all API tests"
	$(PYTEST) tests/test_api.py

allure_report:
	@echo "Generating Allure report"
	$(PYTEST) --alluredir=$(ALLURE_DIR)
	allure serve $(ALLURE_DIR)
