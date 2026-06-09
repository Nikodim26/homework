import csv
import os
from typing import Any


def about_financial_transactions(file_data: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + file_data
    try:
        transactions=[]
        with open(path, "r", encoding="UTF-8") as file:
            reader_csv = csv.DictReader(file, delimiter=';')
            for row_dict in reader_csv:
                transactions.append(row_dict)
            return transactions

    except Exception as e:
        return []


print(about_financial_transactions('transactions.csv'))
# print(about_financial_transactions('transactions_excel.xlsx'))