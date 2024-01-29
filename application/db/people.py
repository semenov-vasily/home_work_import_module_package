from datetime import datetime


def get_employees():
    print('Запуск функции get_employees() из модуля people.py')
    print(f'Текущая дата и время: {datetime.now()}')
    print(f'Текущая дата и время UTC: {datetime.utcnow()}\n')
