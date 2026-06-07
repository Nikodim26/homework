import os
from dotenv import load_dotenv

import requests


def currency_conversion(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    transaction_code = transaction['operationAmount']['currency']['code']
    if transaction_code == "RUB":
        return transaction['operationAmount']['amount']

    if transaction_code == "USD" or transaction_code == "EUR":
        """        
        Загрузка переменных из .env-файла для проформы 
        т.к.    https://apilayer.com/marketplace/exchangerates_data-api мне не доступен
        """
        load_dotenv()
        API_KEY = os.getenv('API_KEY')

        response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js")
        if response.status_code != 200:
            raise ValueError(f"Failed to get currency rate")

        exchange_rate = response.json()['Valute'].get(transaction_code)['Value']
        amount = float(transaction['operationAmount']['amount'])
        return round(exchange_rate * amount, 2)
