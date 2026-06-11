import json
import re

from src.data_search import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import about_financial_transactions_json, about_financial_transactions_csv, \
    about_financial_transactions_xlsx
from src.widget import get_date, mask_account_card


def main() -> None:
    """Производит диалог с клиентом и выводит информацию о транзакциях"""
    #
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
    (по умолчанию 'EXECUTED'): """).upper()

        if not status_val:
            status_val = 'EXECUTED'
            break
        if status_val not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции {status_val} недоступен')
        else:
            break
    print(f'Операции отфильтрованы по статусу "{status_val}"')
    transactions = filter_by_state(transactions, status_val)

    while True:
        answer_to_question_sort = input('Отсортировать операции по дате (Да/Нет) ? ').lower()
        if answer_to_question_sort in ['да', 'нет']:
            break

    answer_to_question_sort = 'да'

    while True:
        answer_to_question_sort_type = input('Отсортировать по возрастанию или по убыванию (возр/убыв) ? ').lower()
        if answer_to_question_sort_type in ['возр', 'убыв']:
            ascending = True if answer_to_question_sort_type == 'убыв' else False
            break


    if answer_to_question_sort == 'да':
        transactions = sort_by_date(transactions, ascending)

    while True:
        answer_to_question_sort_val = input('Выводить только рублевые транзакции (Да/Нет) ? ').lower()
        if answer_to_question_sort_val in ['да', 'нет']:
            is_rub = True if answer_to_question_sort_val == 'да' else False
            break


    if is_rub:
        transactions = process_bank_search(transactions, 'RUB')

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(transactions)}')

    for transaction in transactions:
        dict_str = json.dumps(transaction, ensure_ascii=False)
        dict_str=dict_str.replace('"operationAmount":', '').replace('"currency":', '')
        dict_str = dict_str.replace('currency_', '').replace('Ruble','руб.')
        dict_str = dict_str.replace('NaN', '')

        dict_str = re.sub(r'[\"()\[\]{}]', '', dict_str).split(', ')

        dict_from_json = {}
        for i in dict_str:
            i = i.split(': ')
            dict_from_json[i[0].strip()] = i[1].strip()

        if dict_from_json['description'] =='Открытие вклада':
            line=f'{mask_account_card(dict_from_json['to'])}'
        else:
            line = f'{mask_account_card(dict_from_json['from'])} -> {mask_account_card(dict_from_json['to'])}'

        print(f"""
        {get_date(dict_from_json['date'])} {dict_from_json['description']}
        {line}
        Сумма: {dict_from_json['amount']} {dict_from_json['name']}
        """)