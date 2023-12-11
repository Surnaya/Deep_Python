# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

my_link = 'https://gb.ru/lessons/388829.txt'


def my_func(my_link):
    last_slash = my_link.rfind('/')
    last_point = my_link.rfind('.')
    path, f_name, f_extension = my_link[:last_slash], my_link[last_slash + 1:last_point], my_link[last_point + 1:]
    return f'{path=}, {f_name=}, {f_extension=}'


print(my_func(my_link))
