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
    while True:
        number = input('Введите номер пункта: ')
        if not number.isdigit():
            continue
        number = int(number)
        if number in [1, 2, 3]:
            break

    print(f'Для обработки выбран "{['JSON', 'CSV', 'XLSX'][number - 1]}"-файл.')

    if number == 1:
        transactions = about_financial_transactions_json('operations.json')
    if number == 2:
        transactions = about_financial_transactions_csv('transactions.csv')
    if number == 3:
        transactions = about_financial_transactions_xlsx('transactions_excel.xlsx')

    while True:
        status_val = input("""
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    (по умолчанию 'EXECUTED'): """)

        if not status_val:
            status_val = 'EXECUTED'
            break
        if status_val not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции {status_val} недоступен')
        else:
            break

    print(f'Операции отфильтрованы по статусу "{status_val}"')
    filtered_transactions = filter_by_state(transactions, status_val)
    print(filtered_transactions)


main()
