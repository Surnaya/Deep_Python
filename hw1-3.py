# Программа загадывает число от 0 до 1000. Необходимо угадать число за
# 10 попыток. Программа должна подсказывать “больше” или “меньше” после
# каждой попытки. Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
num = randint(LOWER_LIMIT, UPPER_LIMIT)
my_num = 0
count = 10

while num != my_num and (count > 0):
    my_num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT} '))
    if num > my_num:
        count -= 1
        print(f'Искомое число больше числа {my_num}. Осталось попыток - {count}')
    elif num < my_num:
        count -=1
        print(f'Искомое число меньше числа {my_num}. Осталось попыток - {count}')
    else:
        print(f'Ты угадал!')
else:
    if count == 0:
        print('Твои попытки закончились. Ты проиграл')

