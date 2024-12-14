# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse

def parse():
    parser = argparse.ArgumentParser(
        description='parser',
        epilog='введите число и строку',
    )
    parser.add_argument('-n', '--number', help='Введите число: ', default=1)
    parser.add_argument('-s', '--string', help='Введите строку: ', default='hello world')
    args = parser.parse_args()
    # print(f'{args = }\n{args.count = } {args.weekday = } {args.month = }')
    return args

print(parse())
