import csv
import json
import logging
import os
from typing import Any

import pandas as pd

path = os.path.dirname(os.path.dirname(__file__)) + "\\logs\\utils.log"
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    encoding="UTF8",
    filename=path,
    format="%(levelname)s: %(asctime)s модулем %(name)s %(message)s",
    datefmt="%Y-%m-%d в %H:%M:%S",
)
logger = logging.getLogger("utils")


def about_financial_transactions_json(file_data: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    logger.info(f"получен доступ к данным {file_data}")
    try:
        with open(path, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
            logger.info(f"получена распечатка данных из {file_data}")
            return transactions

    except Exception as e:
        logger.error(f"получена ошибка: {e}")
        return []


def about_financial_transactions_csv(file_data: str) -> Any:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    logger.info(f"получен доступ к данным {file_data}")
    try:
        with open(path, "r", encoding="UTF-8") as file:
            logger.info(f"получена распечатка данных из {file_data}")
            return [row_dict for row_dict in csv.DictReader(file, delimiter=";")]
    except Exception as e:
        logger.error(f"получена ошибка: {e}")
        return []


def about_financial_transactions_xlsx(file_data: str) -> Any:
    """Принимает на вход путь до XLSX-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    logger.info(f"получен доступ к данным {file_data}")
    try:
        reader_xlsx = pd.read_excel(path)
        transactions = reader_xlsx.to_dict("records")
        logger.info(f"получена распечатка данных из {file_data}")
        return transactions

    except Exception as e:
        logger.error(f"получена ошибка: {e}")
        return []