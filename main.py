from datetime import datetime
import configparser
from tqdm import tqdm

from application.db.people import get_employees
from application.salary import calculate_salary


def get_password():
    data = configparser.ConfigParser()
    data.read('password.ini')
    password = data["password"]["password"]
    print(password)


def now_utcnow():
    print('Запуск функции now_utcnow()')
    print(f'Текущая дата и время: {datetime.now()}')
    print(f'Текущая дата и время UTC: {datetime.utcnow()}\n')


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    now_utcnow()
    get_password()
