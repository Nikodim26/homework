import json
import re

from src.data_search import process_bank_search
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import about_financial_transactions_csv
from src.utils import about_financial_transactions_json
from src.utils import about_financial_transactions_xlsx
from src.widget import get_date
from src.widget import mask_account_card


def main() -> None:
    """Производит диалог с клиентом и выводит информацию о транзакциях"""
    #
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("""
            Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла)
    """)
    while True:
        number = input("Введите номер пункта: ")
        if not number.isdigit():
            continue
        elif number in ["1", "2", "3"]:
            print(f'Для обработки выбран "{['JSON', 'CSV', 'XLSX'][int(number) - 1]}"-файл.')
            break

    match number:
        case "1":
            transactions = about_financial_transactions_json("operations.json")
        case "2":
            transactions = about_financial_transactions_csv("transactions.csv")
        case "3":
            transactions = about_financial_transactions_xlsx("transactions_excel.xlsx")

    while True:
        status_val = input("""
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    /'EXECUTED'): """).upper()

        if status_val in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        if status_val == "":
            status_val = "EXECUTED"
            break
        print(f"Статус операции {status_val} недоступен")

    transactions = filter_by_state(transactions, status_val)
    print(f'Операции отфильтрованы по статусу "{status_val}"')

    while True:
        answer_to_question_sort = input("Отсортировать операции по дате (Да/Нет) /Да ? ").lower()
        if answer_to_question_sort in ["да", "нет"]:
            break
        if answer_to_question_sort == "":
            answer_to_question_sort = "да"
            break

    while True:
        answer_to_question_sort_type = input(
            "Отсортировать по возрастанию или по убыванию (возр/убыв) /убыв ? "
        ).lower()
        if answer_to_question_sort_type in ["возр", "убыв"]:
            break
        if answer_to_question_sort_type == "":
            answer_to_question_sort_type = "убыв"
            break

    ascending = True if answer_to_question_sort_type == "убыв" else False
    if answer_to_question_sort == "да":
        transactions = sort_by_date(transactions, ascending)

    while True:
        answer_to_question_sort_val = input("Выводить только рублевые транзакции (Да/Нет) /да ? ").lower()
        if answer_to_question_sort_val in ["да", "нет"]:
            break
        if answer_to_question_sort_val == "":
            answer_to_question_sort_val = "да"
            break

    if answer_to_question_sort_val == "да":
        transactions = process_bank_search(transactions, "RUB")

    while True:
        answer_to_question_sort_word = input(
            "Отфильтровать список транзакций по определенному слову в описании Да/Нет ? /Да"
        )
        if answer_to_question_sort_word in ["да", "нет"]:
            break
        if answer_to_question_sort_word == "":
            answer_to_question_sort_word = "да"
            break

    if answer_to_question_sort_word == "да":
        word_for_sort = input("Введите слово для сортировки ")
        transactions = process_bank_search(transactions, word_for_sort)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        dict_str = json.dumps(transaction, ensure_ascii=False)
        dict_str = dict_str.replace('"operationAmount":', "").replace('"currency":', "")
        dict_str = dict_str.replace("currency_", "").replace("Ruble", "руб.")
        dict_str = dict_str.replace("NaN", "")

        dict_str = re.sub(r"[\"()\[\]{}]", "", dict_str).split(", ")

        dict_from_json = {}
        for i in dict_str:
            i = i.split(": ")
            dict_from_json[i[0].strip()] = i[1].strip()

        if dict_from_json["description"] == "Открытие вклада":
            line = f"{mask_account_card(dict_from_json['to'])}"
        else:
            line = f"{mask_account_card(dict_from_json['from'])} -> {mask_account_card(dict_from_json['to'])}"

        print(f"""
        {get_date(dict_from_json['date'])} {dict_from_json['description']}
        {line}
        Сумма: {dict_from_json['amount']} {dict_from_json['name']}
        """)


main()
