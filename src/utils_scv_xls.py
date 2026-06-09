import csv
import os
from typing import Any

import pandas as pd


def about_financial_transactions_csv(file_data: str) -> Any:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    try:
        with open(path, "r", encoding="UTF-8") as file:
            print(next(csv.DictReader(file, delimiter=";")))
            return [row_dict for row_dict in csv.DictReader(file, delimiter=";")]
    except Exception as e:
        print(e)
        return []


def about_financial_transactions_xlsx(file_data: str) -> Any:
    """Принимает на вход путь до XLSX-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    try:
        reader_xlsx = pd.read_excel(path)
        transactions = reader_xlsx.to_dict("records")
        return transactions

    except Exception as e:
        print(e)
        return []


about_financial_transactions_csv("transactions.csv")
