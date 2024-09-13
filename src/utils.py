import datetime
import logging
import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY_CUR = os.getenv("API_KEY_CUR")

SP_500_API_KEY = os.getenv("SP_500_API_KEY")

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler(abs_file_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data(data: str) -> datetime.datetime:
    """Функция преобразования даты"""
    logger.info(f"Получена строка даты: {data}")
    try:
        data_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
        logger.info(f"Преобразована в объект datetime: {data_obj}")
        return data_obj
    except ValueError as e:
        logger.error(f"Ошибка преобразования даты: {e}")
        raise e


def transaction_excel(file_path):
    """Функция принимает на вход путь до файла и возвращает дата-фрейм"""

    logger.info(f"Вызвана функция получения транзакций из файла {file_path}")
    try:
        df_transactions = pd.read_excel(file_path)
        logger.info(f"Файл {file_path} найден, данные о транзакциях получены")
    except FileNotFoundError:
        logger.info(f"Файл {file_path} не найден")
    raise


def reader_transaction_excel(file_path):
    """Функция читает .xlsx файл и возвращает список словарей"""
    df = pd.read_excel(file_path)
    result = df.apply(
        lambda row: {
            "Дата платежа": row["Дата платежа"],
            "Статус": row["Статус"],
            "Сумма платежа": row["Сумма платежа"],
            "Валюта платежа": row["Валюта платежа"],
            "Категория": row["Категория"],
            "Описание": row["Описание"],
            "Номер карты": row["Номер карты"],
        },
        axis=1,
    ).tolist()
    return result
