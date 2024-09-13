import json

import pandas as pd

from src.utils import reader_transaction_excel
from src.views import cards_dicts, currency_rates, greeting, price_stock, top_transaction


def main(file_path, currencies, stocks):
    """Главная функция, делающая вывод на главную страницу"""
    greetings = greeting()
    file_read = pd.read_excel(file_path)
    file_data = pd.DataFrame(file_read)
    file = reader_transaction_excel(file_path)
    card = cards_dicts(file)
    top = top_transaction(file_data)
    currency_rate = currency_rates(currencies)
    stock = price_stock(stocks)
    date_json = json.dumps(
        {
            "greeting": greetings,
            "cards": card,
            "top_transactions": top,
            "currency_rates": currency_rate,
            "stock_prices": stock,
        },
        indent=4,
        ensure_ascii=False,
    )
    return date_json
