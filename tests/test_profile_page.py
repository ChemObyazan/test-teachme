import pytest
from pages.profile_page import ProfilePage

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

def test_profile_info_visibility(profile_page):
    """Проверка видимости информации профиля."""
    profile_page.driver.get('https://www.traektoria.ru/profile')
    assert profile_page.is_profile_info_visible()
