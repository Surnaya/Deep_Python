# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
#
# При переименовании в конце имени добавляется порядковый номер.
#
# принимать параметр количество цифр в порядковом номере.
#
# принимать параметр расширение исходного файла.
#
# Переименование должно работать только для этих файлов внутри каталога.
#
# принимать параметр расширение конечного файла.
#
# принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами.

from pathlib import Path
import os


def rename_files(new_name: str, cnt_name: int, origin_extension: str, final_extension: str, range_name: list, path=os.getcwd()):
    counter = 1
    for obj in os.listdir(path):
        if obj.endswith(origin_extension):
            old_name = obj.split('.')[0][range_name[0]:range_name[1]]
            file_numb = str(counter).zfill(cnt_name)
            file_name = f'{old_name}{new_name}{file_numb}.{final_extension}'
            os.rename(obj, file_name)
            counter +=1


if __name__ == '__main__':
    rename_files('file', 2, 'txt', 'md', [1,2])