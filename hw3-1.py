# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42, 7]
COUNT = 2
new_data = []

for item in set(data):
    if data.count(item) >= COUNT:
        new_data.append(item)

print(new_data)