import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    """Фикстура для инициализации веб-драйвера."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
