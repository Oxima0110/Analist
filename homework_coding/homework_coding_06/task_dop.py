# Напишите программу вычисления арифметического выражения
# заданного строкой.
# Используйте операции +,-,/,*. приоритет операций
# стандартный.
# Дополнительное задание: Добавьте возможность использования
# скобок, меняющих приоритет операций
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

from os import system
system("cls")

import function as fun

def get_str(input_string:str)->str:
    while True:
        str = input(input_string)
        str = fun.remove_spaces_in_string(str)
        if str == '':
            print('Пустая строка')
            continue
        count_1 = str.count('(')
        count_2 = str.count(')')
        if count_1 != count_2:
            print('Некорректная запись скобок')
            continue
        
        text = str
        text = fun.remove_symbols_in_string(text)
        if  not text.isdigit():
            print('Неправильный ввод: нужны числа')
            continue
        text = str
        text = fun.remove_bracket_in_string(text)
        if not text[0].isdigit() or not text[-1].isdigit():
            print('Недостаточно числовых данных')
            continue
        return str

def parse(s: str)-> list:
    result = []
    digit = ''
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symbol)
    if digit:
        result.append(float(digit))
    temp_lst = [y for x, y in zip(result, list(range(len(result)))) if x == '-']
    # print(temp_lst)
    for i in temp_lst:
        if type (result[i - 1]) != float:
            temp = result[ i + 1]
            result = result[:i] + [temp * -1] + result[i + 2:]        
    return result

def calculate(lst: list) -> float:
    result = 0.0
    for char in lst:
        if char == '*':
            index = lst.index('*')
            result = lst[index - 1] * lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
        elif char == '/':
            index = lst.index('/')
            result = lst[index - 1] / lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    for char in lst:
        if char == '+':
            index = lst.index('+')
            result = lst[index - 1] + lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
        elif char == '-' :
            index = lst.index('-')
            result = lst[index - 1] - lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

def bracket_opening(lst: list) -> list:
    while '(' in lst:
        close = lst.index(')')
        temp_lst = [y for x, y in zip(lst[:close], list(range(close-1))) if x == '(']
        open = temp_lst[-1]        
        lst = lst[:open] + [calculate(lst[open + 1: close])] + lst[close + 1:]
    return lst    



string = get_str('Введите выражение:\n')
list_num = parse(string)
list_result = bracket_opening(list_num)
result = calculate(list_result)
print(f'{string} = {result}')
