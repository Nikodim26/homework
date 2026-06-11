import logging
import os

path = os.path.dirname(os.path.dirname(__file__)) + "\\logs\\masks.log"
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    encoding="UTF8",
    filename=path,
    format="%(levelname)s: %(asctime)s модулем %(name)s %(message)s",
    datefmt="%Y-%m-%d в %H:%M:%S",
)
logger = logging.getLogger("masks")


def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты в виде строки и возвращает маску номера по правилу
    "XXXX XX** **** XXXX" """
    logger.info(f"получен номер карты: {number}")

    number = number[:6] + "******" + number[-4:]
    number = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[-4:]
    logger.info(f"выдана маска карты: ->>> {number}")
    return number


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде строки и возвращает маску номера по правилу
    "**XXXX" """
    logger.info(f'получен номер счета: {account} и получена маска: ->>> {"**" + account[-4:]}')
    return "**" + account[-4:]
