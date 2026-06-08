from typing import Any

import requests


def currency_conversion(transaction: dict) -> Any:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        transaction_code = transaction["operationAmount"]["currency"]["code"]
        if transaction_code == "RUB":
            return float(transaction["operationAmount"]["amount"])

        if transaction_code == "USD" or transaction_code == "EUR":
            """
            Загрузка переменных из .env-файла для проформы
            load_dotenv()
            API_KEY = os.getenv("API_KEY")
            т.к.    https://apilayer.com/marketplace/exchangerates_data-api мне не доступен
            """

            response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
            if response.status_code != 200:
                raise ValueError("Failed to get currency rate")

            exchange_rate = response.json()["Valute"].get(transaction_code)["Value"]
            amount = float(transaction["operationAmount"]["amount"])

            return round(exchange_rate * amount, 2)
    except Exception:
        print('Что-то пошло не так с транзакцией')
