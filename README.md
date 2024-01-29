# Домашнее задание к лекции 1. «Import. Module. Package»

1. Разработать структуру программы «Бухгалтерия»:
* [main.py](main.py)
* [salary.py](application%2Fsalary.py)
* [people.py](application%2Fdb%2Fpeople.py)

Main.py — основной модуль для запуска программы.

В модуле salary.py функция calculate_salary.

В модуле people.py функция get_employees.

2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.

```
if __name__ == '__main__':
```
В функции добавлен вывод сообщения о запуске

3. Импортирован модуль ***datetime***. При вызове функций модуля ***main.py*** выводится текущая дата.

4. Импортирован модуль ***tqdm*** и ***configparser***. Создан файл ***requirements.txt***

5. Создан рядом с файлом main.py модуль dirty_main.py и импортированы
все функции с помощью конструкции (необязательное задание).

```
from package.module import *
```