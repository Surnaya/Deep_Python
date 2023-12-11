# Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fibo(num):
    fib1, fib2 = 0, 1
    for _ in range(num):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


print(*fibo(12))