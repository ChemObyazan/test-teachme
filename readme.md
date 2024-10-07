# ������ ������������� ������������ ��� ����� ����������

## ��������
������ ������������� ������������, ���������� UI � API ����� ��� ����� [����������](https://www.traektoria.ru/). ������ ���������� � �������������� Page Object Model (POM).

### ��������� �������:
- `locators/` � �������� ��� �������
- `pages/` � ���������� �������
- `tests/` � ����� ��� ������� � API
- `conftest.py` � ��������� �������� � �������
- `Makefile` � ������� ��� ������� ������
- `requirements.txt` � ����������� �������

### ��������� � ������:
1. ����������� �����������:
```bash
git clone <repository-url>

2. ��������� ������������:
pip install -r requirements.txt

3. ��������� ��� �����.
make test_all

4. ��������� UI �����:
make test_ui

5. ��������� API �����:
make test_api

6. ������������� ����� Allure
make allure_report

6.1 **����������� ������ � Allure**:
��� ��������� ������� Allure, ����� ���������, ��� Allure ���������� � �������.

#### ��������� Allure:
```bash
choco install allure  # ��� Windows