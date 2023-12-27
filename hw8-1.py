# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами разных форматов.
import csv
import json
import os
import pickle
from pathlib import Path


def get_size(path):
    size = 0
    for dir_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            size += os.path.getsize(file_path)
    return size


folder_list = []


def folder_trav(path) -> None:
    global folder_list
    for name in os.listdir(path):
        if os.path.isdir(path + '/' + name):
            folder_list.append({'type': 'directory',
                                'name': name,
                                'main_dir': path,
                                'size': get_size(path + '/' + name)})

            folder_trav(path + '/' + name)
        elif os.path.isfile(path + '/' + name):
            folder_list.append({'type': 'file',
                                'name': name,
                                'main_dir': path,
                                'size': os.path.getsize(path + '/' + name)})

        with open("folder_list.json", "w") as json_file:
            json.dump(folder_list, json_file)

        with open("folder_list.csv", "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=folder_list[0].keys())
            writer.writeheader()
            writer.writerows(folder_list)

        with open("folder_list.pickle", "wb") as pickle_file:
            pickle.dump(folder_list, pickle_file)


if __name__ == '__main__':
    folder_trav('/Users/surnaya.m/PycharmProjects/Dive_into_Python/seminar_8')
