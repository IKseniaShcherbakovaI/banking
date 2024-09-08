import re
import os
import pandas as pd
import json
import logging

# получение пути до файла с транзакциями
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "..//data//operations.xlsx")
abs_file_path = os.path.abspath(rel_file_path)
# получение пути к файлам логов
current_dir_log = os.path.dirname(os.path.abspath(__file__))
rel_file_path_log = os.path.join(current_dir_log, "..//logs//services.py.log")
logs_file_path = os.path.abspath(rel_file_path_log)
logger = logging.getLogger("services")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(logs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
def transaction_excel(path_excel):
    """
    Функция принимающая на вход путь до excel файла и возвращающая список словарей с данными о финансовых транзакциях
    """
    logger.info(f"Ищем файл по указанному пути {path_excel}")
    if not path_excel:
        logger.info(f"файл не найден")
        return []
    try:
        logger.info("открываем файл по указанному пути и получаем транзакции")
        df = pd.read_excel(path_excel)
        return df.to_dict(orient="records")
    except Exception:
        return []


result = transaction_excel(abs_file_path)


def transactions_by_phone_number(transaction):
    """
    функция для поиска в списке словарей операций по заданной строке
    """
    result_search = []
    logger.info("получаем информацию по ключу")
    for i in transaction:
        # logger.info("получаем информацию по ключу")
        our_str = i['Описание']
        if re.findall('.+7 9', our_str, re.IGNORECASE):
            result_search.append(i)
    logger.info("поиск строки выполнен, обрабатываем результат")
    # data = json.dumps(result_search, indent=3, ensure_ascii=False)
    data = json.dumps(result_search, ensure_ascii=False)
    # print(len(result_search))
    return data
    # return result_search


print(transactions_by_phone_number(result))
