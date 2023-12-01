# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

HEX = 16

num = int(input('введите число '))
result: str = ''
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
test_num: int = num
while test_num > 0:
    result = digits[test_num % HEX] + result
    test_num //= HEX
print(f'Число {num} в шестнадцатиричном представлении = {result}')

print(f'{hex(num)=}')


