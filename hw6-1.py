# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
from module_date import check_date

if __name__ == '__main__':
    print(check_date(*(param for param in argv[1:])))
