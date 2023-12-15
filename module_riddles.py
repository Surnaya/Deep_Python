# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

__all__ = ['riddle', 'storage', 'show_results']

_data = {}


def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка №{nn}: ').lower()
        if ans in answers:
            return nn
    return 0


def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn


def show_results():
    res = (f'Загадку "{puzzle}" разгадали с {nn}й попытки' if nn > 0
           else f'Загадку "{puzzle}" не разгадали'
           for puzzle, nn in _data.items())
    print(*res, sep='\n')


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка', 'сосна'],
        'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
        'Не лает, не кусает, в дом не пускает': ['замок', 'домофон']
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(f'Угадал с {result}й попытки!' if result > 0 else 'Не угадал!')
        save_results(puzzle, result)


if __name__ == '__main__':
    storage()
    show_results()
