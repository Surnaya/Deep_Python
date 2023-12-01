# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions
import math
import fractions

a = input('введите дробное число a ')
b = input('введите дробное число b ')

num_a, denom_a = map(int, a.split("/"))
num_b, denom_b = map(int, b.split("/"))

# сумма дробей
sum_num = num_a * denom_b + num_b * denom_a
sum_denom = denom_a * denom_b
gcd_sum = math.gcd(sum_num, sum_denom)
new_sum_num = sum_num // gcd_sum
new_sum_denom = sum_denom // gcd_sum

# произведение дробей
mult_num = num_a * num_b
mult_demon = denom_a * denom_b
gcd_mult = math.gcd(mult_num, mult_demon)
new_mult_num = mult_num // gcd_mult
new_mult_denom = mult_demon // gcd_mult

sum_fractions = fractions.Fraction(num_a, denom_a) + fractions.Fraction(num_b, denom_b)
mult_fractions = fractions.Fraction(num_a, denom_a) * fractions.Fraction(num_b, denom_b)

print(f'Сумма дробей {a} и {b} = {new_sum_num}/{new_sum_denom}. Проверка через модуль fraction = {sum_fractions}')
print(f'Произведение дробей {a} и {b} = {new_mult_num}/{new_mult_denom}. Проверка через модуль fraction = {mult_fractions}')