"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
"""
Функция check_data принимает два параметра - путь к файлу и список функций (валидаторов).
Вы должны:
	•	прочитать данные из файла data.txt
	•	проверить каждую строку согласно правилам. Каждое правило представляет собой функцию, которая выполняет определенную проверку
	•	записать отчет в txt-файл и вернуть абсолютный путь к этому файлу. Для каждой строки вы должны сообщить о ней, если она не соответствует по крайней мере одному правилу, а также добавить причину - имя валидатора, который не прошел проверку (если несколько правил не прошли проверку, следует указать имя первого неудачного валидатора)
Корректная строка должна содержать 5 элементов в следующем порядке:
email, amount, currency, account, date.

Также необходимо реализовать как минимум два правила:
	•	функция validate_line должна проверять, содержит ли строка 5 элементов
	•	функция validate_date должна проверять, является ли дата допустимой. В нашем случае допустимой датой будет любая дата, следующая за шаблоном DDDD-DD-DD (четыре цифры - две цифры - две цифры). Дата всегда присутствует в строке, даже если эта строка повреждена каким-либо другим образом.
	•	Не стесняйтесь добавлять больше правил!

    For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""


from typing import Callable, Iterable
import re
import os


def validate_line(line: str) -> bool:
    return len(line.split()) == 5


def validate_date(date: str) -> bool:
    return re.match('^\d{4}-\d{2}-\d{2}$', date)


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    reportpath = './hw3/data/report.txt'
    with open(filepath, 'r') as file, open(reportpath, 'w') as report:
        for line in file:
            line = line.strip()
            failed = False
            for validator in validators:
                if not validator(line):
                    report.write(f"{line} {validator.__name__}\n")
                    failed = True
                    break
                if not failed:
                    report.write(f"{line}\n")
    return os.path.abspath(reportpath)


filepath = './hw3/data/data.txt'
validators = [validate_line, validate_date]
