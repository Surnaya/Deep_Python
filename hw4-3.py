# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

account = decimal.Decimal(0)
count = 1


def menu():
    global account
    global count
    while True:
        text = f'Какую операцию вы хотите совершить?: \n' \
               f'1 - пополнить счет\n' \
               f'2 - снять деньги\n' \
               f'3 - выйти'
        print(text)
        choice = int(input())
        richness_tax()
        func_bonus()
        if choice == 1:
            deposit_money(enter_amount())
        elif choice == 2:
            withdraw_money(enter_amount())
        elif choice == 3:
            print(f'Возьмите карту. На вашей карте {account} у.е.')
            break

# функция для ввода суммы на снятие и пополнение
def enter_amount():
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f' Введите сумму кратную 50: '))
        return amount

# функция для пополнения баланса
def deposit_money(amount):
    global account
    global count
    account += amount
    count += 1
    print(f'Пополнение карты на сумму {amount} у.е. На вашей карте {account} y.e.')
    return account

# функция для снятия средств
def withdraw_money(amount):
    global account
    global count
    if account >= amount + withdraw_tax(amount):
        count += 1
        account -= (amount + withdraw_tax(amount))
        print(
            f'Снятие с карты {amount} y.e. Комиссия за снятие {withdraw_tax(amount)} y.e. На вашей карте осталось {account} у.е.')
    else:
        print(f'Недостаточно средств. На вашей карте осталось {account} у.е.')
    return account

# функция для подсчета комиссии
def withdraw_tax(amount):
    min_removal = 30
    max_removal = 600
    withdraw_percent = decimal.Decimal(15) / decimal.Decimal(1000)
    tax = (min_removal if amount * withdraw_percent < min_removal else
           max_removal if amount * withdraw_percent > max_removal else amount * withdraw_percent)
    return tax

# функция для подсчета налога на богатство
def richness_tax():
    global account
    if account >= decimal.Decimal(5_000_000):
        percent = account * (decimal.Decimal(10) / decimal.Decimal(100))
        account -= percent
        print(f'Удержан налог на богатство 10% = {percent} y.e. На вашей карте осталось {account} у.е.')
    return account

# функция для начисления бонуса
def func_bonus():
    global count
    global account
    if count % 3 == 0:
        bonus_percent = account * (decimal.Decimal(3) / decimal.Decimal(100))
        account += bonus_percent
        print(f'На счет начислен бонус 3 % = {bonus_percent} y.e. На вашей карте {account} y.e.')
    return account


menu()
