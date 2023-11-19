# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 1
UPPER_LIMIT = 100000
num = 0
result = ''

while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT} '))
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count = count + 1
    if count <= 0:
        result = f'Вы ввели число {num}. Это простое число'
    else:
        result = f'Вы ввели число {num}. Это составное число'
print(result)
