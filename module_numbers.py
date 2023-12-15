# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

__all__ = ['guess']

from random import randint


def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = randint(lower, upper)
    for num in range(1, count + 1):
        answer = int(input(f'Попытка номер {num}, введите число от {lower} до {upper}: '))
        if answer > number:
            print(f'Число {answer} больше загаданного')
        elif answer < number:
            print(f'Число {answer} меньше загаданного')
        else:
            return True
    return False


if __name__ == '__main__':
    print(guess())
