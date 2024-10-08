import pytest
from src.services import transactions_by_phone_number

@pytest.fixture()
def test_df():
    trans_1 = [{"Дата операции": "18.11.2021 21:15:27", "Дата платежа": "19.11.2021",
              "Номер карты": 'None', "Статус": "OK", "Сумма операции": -200.0,
              "Валюта операции": "RUB", "Сумма платежа": -200.0, "Валюта платежа": "RUB",
              "Кэшбэк": 'None', "Категория": "Мобильная связь", "MCC": 'None',
              "Описание": "Тинькофф Мобайл ssss",
              "Бонусы (включая кэшбэк)": 2, "Округление на инвесткопилку": 0,
              "Сумма операции с округлением": 200.0},
             {"Дата операции": "18.11.2021 21:15:27",
              "Дата платежа": "19.11.2021", "Номер карты": 'None',
              "Статус": "OK", "Сумма операции": 200.0, "Валюта операции": "RUB",
              "Сумма платежа": 200.0, "Валюта платежа": "RUB", "Кэшбэк": 'None',
              "Категория": "Пополнения", "MCC": 'None', "Описание": "Тинькофф Мобайл sss",
              "Бонусы (включая кэшбэк)": 0, "Округление на инвесткопилку": 0,
              "Сумма операции с округлением": 200.0},
             {"Дата операции": "29.09.2021 18:48:24", "Дата платежа": "29.09.2021",
              "Номер карты": 'None', "Статус": "OK", "Сумма операции": -100.0, "Валюта операции": "RUB",
              "Сумма платежа": -100.0, "Валюта платежа": "RUB", "Кэшбэк": 'None',
              "Категория": "Мобильная связь", "MCC": 'None', "Описание": "Я МТС +7 921 11-22-33",
              "Бонусы (включая кэшбэк)": 1, "Округление на инвесткопилку": 0,
              "Сумма операции с округлением": 100.0}]
    return trans_1

@pytest.fixture()
def test_df2():
    test_dict = [{"Дата операции": "18.11.2021 21:15:27", "Дата платежа": "19.11.2021",
                  "Номер карты": 'None', "Статус": "OK", "Сумма операции": -200.0,
                  "Валюта операции": "RUB", "Сумма платежа": -200.0, "Валюта платежа": "RUB",
                  "Кэшбэк": 'None', "Категория": "Мобильная связь", "MCC": 'None',
                  "Описание": "Тинькофф Мобайл ssss",
                  "Бонусы (включая кэшбэк)": 2, "Округление на инвесткопилку": 0,
                  "Сумма операции с округлением": 200.0},
                 {"Дата операции": "18.11.2021 21:15:27",
                  "Дата платежа": "19.11.2021", "Номер карты": 'None',
                  "Статус": "OK", "Сумма операции": 200.0, "Валюта операции": "RUB",
                  "Сумма платежа": 200.0, "Валюта платежа": "RUB", "Кэшбэк": 'None',
                  "Категория": "Пополнения", "MCC": 'None', "Описание": "Тинькофф Мобайл sss",
                  "Бонусы (включая кэшбэк)": 0, "Округление на инвесткопилку": 0,
                  "Сумма операции с округлением": 200.0},
                 {"Дата операции": "29.09.2021 18:48:24", "Дата платежа": "29.09.2021",
                  "Номер карты": 'None', "Статус": "OK", "Сумма операции": -100.0, "Валюта операции": "RUB",
                  "Сумма платежа": -100.0, "Валюта платежа": "RUB", "Кэшбэк": 'None',
                  "Категория": "Мобильная связь", "MCC": 'None', "Описание": "dddd",
                  "Бонусы (включая кэшбэк)": 1, "Округление на инвесткопилку": 0,
                  "Сумма операции с округлением": 100.0}
                 ]
    return test_dict
def test_transactions_by_phone_number(test_df):
    assert transactions_by_phone_number(test_df) == ('[{"Дата операции": "29.09.2021 18:48:24", "Дата платежа": "29.09.2021", '
                                                    '"Номер карты": "None", "Статус": "OK", "Сумма операции": -100.0, "Валюта операции": "RUB", '
                                                    '"Сумма платежа": -100.0, "Валюта платежа": "RUB", "Кэшбэк": "None", '
                                                    '"Категория": "Мобильная связь", "MCC": "None", "Описание": "Я МТС +7 921 11-22-33", '
                                                    '"Бонусы (включая кэшбэк)": 1, "Округление на инвесткопилку": 0, '
                                                    '"Сумма операции с округлением": 100.0}]')



def test_transactions_by_phone_number_2(test_df2):
    assert transactions_by_phone_number(test_df2) == '[]'
