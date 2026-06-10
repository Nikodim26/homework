import json

from src.utils import about_financial_transactions_xlsx, about_financial_transactions_csv, \
    about_financial_transactions_json


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""

    return [dict_data for dict_data in data if search_string in json.dumps(dict_data, ensure_ascii=False)]


def process_bank_operations(data: list[dict], categories: list):
    descriptions = set(dict_data.get('description') for dict_data in data if dict_data.get('description'))
    result = {}
    for description in descriptions:
        if description in categories:
            result[description] = len(process_bank_search(data, description))

    return result


if __name__ == '__main__':
    # a = process_bank_search(about_financial_transactions_json('operations.json'), "Перевод организации")
    # # a=process_bank_search(about_financial_transactions_csv('transactions.csv'),'USD')
    # a=process_bank_search(about_financial_transactions_xlsx("transactions_excel.xlsx"),'EUR')
    #
    # with open('dgdgdfgfd.json', 'w', encoding="UTF-8") as f:
    #     json.dump(a, f, ensure_ascii=False)
    descriptions = ['Перевод с карты на счет', 'Перевод организации', 'Перевод с карты на карту', 'Перевод со счета на счет', 'Открытие вклада']
    # print(process_bank_operations(about_financial_transactions_json('operations.json'), descriptions))
    # print(process_bank_operations(about_financial_transactions_csv('transactions.csv'), descriptions))
    print(process_bank_operations(about_financial_transactions_xlsx("transactions_excel.xlsx"), descriptions))
