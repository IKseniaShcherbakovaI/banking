import datetime
import json
import logging
import os
import urllib.request

import requests
from dotenv import load_dotenv

# API
load_dotenv(".env.example")
API_KEY = os.getenv("API_KEY")
SP_500_API_KEY = os.getenv("SP_500_API_KEY")

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/views.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("views.log")
file_handler = logging.FileHandler(abs_file_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def greeting():
    """
    Функция выдающая приветствие в зависимости от времени суток
    """
    logger.info("Начало работы функции greeting")
    time = datetime.datetime.now()
    now_time = datetime.datetime.strftime(time, "%H")
    logger.info("Функция greeting завершила работу")
    if 0 <= int(now_time) < 6:
        return "Доброй ночи"
    elif 6 <= int(now_time) < 12:
        return "Доброе утро"
    elif 12 <= int(now_time) < 18:
        return "Добрый день"
    elif 18 <= int(now_time) < 24:
        return "Добрый вечер"


def cards_dicts(my_list):
    """Функция создания информации по каждой карте"""
    logger.info("Начало работы функции cards_dicts")
    cards = {}
    result = []
    for i in my_list:
        if type(i["Номер карты"]) is float:
            continue
        elif i["Сумма платежа"] == "nan":
            continue
        else:
            if i["Номер карты"][1:] in cards:
                cards[i["Номер карты"][1:]] += float(str(i["Сумма платежа"])[1:])
            else:
                cards[i["Номер карты"][1:]] = float(str(i["Сумма платежа"])[1:])
    for k, v in cards.items():
        result.append({"last_digits": k, "total_spent": round(v, 2), "cashback": round(v / 100, 2)})
    logger.info("Функция cards_dicts завершила работу")
    return result


def top_transaction(transactions):
    """Функция вывода топ 5 транзакций по сумме платежа"""
    logger.info("Начало работы функции top_transaction")
    top_transaction = transactions.sort_values(by="Сумма платежа", ascending=True).iloc[:5]
    logger.info("Получен топ транзакций")
    result_top_transaction = top_transaction.to_dict(orient="records")
    top_transaction_list = []
    for transaction in result_top_transaction:
        top_transaction_list.append(
            {
                "date": str(
                    (datetime.datetime.strptime(transaction["Дата операции"][:10], "%d.%m.%Y"))
                    .date()
                    .strftime("%d.%m.%Y")
                ).replace("-", "."),
                "amount": transaction["Сумма платежа"],
                "category": transaction["Категория"],
                "description": transaction["Описание"],
            }
        )
    logger.info("Список сформирован, функция завершила работу")
    return top_transaction_list


def currency_rates(currency: list) -> list[dict]:
    """Функция запроса курса валют"""
    logger.info("Начало работы функции (currency_rates)")
    api_key = API_KEY
    # print(api_key)
    result = []
    for i in currency:
        # https: // v6.exchangerate - api.com / v6 / ce8bb57ccc6e65c392e338df / latest / USD
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{i}"
        with urllib.request.urlopen(url) as response:
            body_json = response.read()
        body_dict = json.loads(body_json)
        result.append({"currency": i, "rate": round(body_dict["conversion_rates"]["RUB"], 2)})

    logger.info("Создание списка словарей для функции - currency_rates")

    logger.info("Окончание работы функции - currency_rates")
    return result


def price_stock(stocks: list) -> list:
    """Функция для получения данных об акциях из списка S&P500"""
    logger.info("Начало работы функции (get_price_stock)")
    api_key = SP_500_API_KEY
    stock_prices = []
    logger.info("Функция обрабатывает данные транзакций.")
    for stock in stocks:
        logger.info("Перебор акций в списке 'stocks' в функции (get_price_stock)")
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
        response = requests.get(url, timeout=5, allow_redirects=False)
        result = response.json()

        stock_prices.append({"stock": stock, "price": round(float(result["Global Quote"]["05. price"]), 2)})
    logger.info("Функция get_price_stock успешно завершила свою работу")
    return stock_prices
