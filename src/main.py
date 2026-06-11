from src.processing import filter_by_state
from src.utils import about_financial_transactions_json, about_financial_transactions_csv, \
    about_financial_transactions_xlsx


def main() -> dict:
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print("""
            Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла)
    """)

    file_types = ['JSON', 'CSV', 'XLSX']

    # number = int(input('Введите номер пункта: '))
    number = 1
    print(f'Для обработки выбран "{file_types[number - 1]}"-файл.')

    if number == 1:
        transactions = about_financial_transactions_json('operations.json')
    if number == 2:
        transactions = about_financial_transactions_csv('transactions.csv')
    if number == 3:
        transactions = about_financial_transactions_xlsx('transactions_excel.xlsx')

    status = ['EXECUTED', 'CANCELED', 'PENDING']
    # while True:
    #     status_val = input("""
    #     Введите статус, по которому необходимо выполнить фильтрацию.
    #     Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    #     """)
    #     if status_val not in status:
    #         print(f'Статус операции {status_val} недоступен')
    #     else:
    #         break
    status_val = 'CANCELED'
    print(f'Операции отфильтрованы по статусу "{status_val}"')
    filtered_transactions = filter_by_state(transactions, status_val)
    print(filtered_transactions)



main()
