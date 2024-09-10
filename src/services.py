import re
import os
import json
import logging


# получение пути к файлам логов
current_dir_log = os.path.dirname(os.path.abspath(__file__))
rel_file_path_log = os.path.join(current_dir_log, "..//logs//services.log")
logs_file_path = os.path.abspath(rel_file_path_log)
logger = logging.getLogger("services")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(logs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def transactions_by_phone_number(transaction):
    """
    функция для поиска в списке словарей операций по заданной строке
    """
    result_search = []
    logger.info("получаем информацию по ключу")
    for i in transaction:
        our_str = i['Описание']
        if re.findall('.+7 9', our_str, re.IGNORECASE):
            result_search.append(i)
    logger.info("поиск строки выполнен, обрабатываем результат")
    data = json.dumps(result_search, ensure_ascii=False)
    return data
