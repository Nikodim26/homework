import json
import os


def about_financial_transactions(path_json: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    path = os.path.dirname(os.path.dirname(__file__)) + '\\data\\' + path_json
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            transactions = json.load(file)
            return transactions
    except Exception as e:
        print(e)
        return []