# ������������ ����� ����������
https://www.traektoria.ru/

## ��������� �������

������  ������� �� ����������� Page Object Model 


- `pages/` - �������� �������� ����� � ������ ��� �������������� � ���������� ���� ��������.
  - `base_page.py` - ������� ��������, �������� ����� ������ ��� ���� �������.
  - `home_page.py` - ������� ��������.
  - `category_page.py` - �������� ���������.
  - `product_page.py` - ��������.
  - `cart_page.py` - �������.
  - `checkout_page.py` - ���������� ������.
  - `login_page.py` - �������� �����.
  - `profile_page.py` - ������ ������������.
  - `about_page.py` - �������� "� ���".
  - `contacts_page.py` - �������� "��������".
- `tests/` - �������� ����� ��� ������ ��������.
  - `test_home_page.py` - ����� ��� ������� ��������.
  - `test_category_page.py` - ����� ��� �������� ���������.
  - `test_product_page.py` - ����� ��� �������� ��������.
  - `test_cart_page.py` - ����� ��� �������� �������.
  - `test_checkout_page.py` - ����� ��� �������� ���������� ������.
  - `test_login_page.py` - ����� ��� �������� �����.
  - `test_profile_page.py` - ����� ��� �������� ������� ������������.
  - `test_about_page.py` - ����� ��� �������� "� ���".
  - `test_contacts_page.py` - ����� ��� �������� "��������".
- `conftest.py` - �������� �������� ��� Pytest.
- `pytest.ini` - ���������������� ���� ��� Pytest.

## ��������� ������������
pip install -r requirements.txt

##������ ������
pytest

##���������� �������
allure serve /path/to/your/report/directory