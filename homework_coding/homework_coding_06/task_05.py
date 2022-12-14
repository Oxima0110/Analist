# 5- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from os import system
system("cls")
import function as fun


# list_number = [2, 3, 4, 5, 6]

number = abs(fun.get_number('Введите размер списка, это должно быть целое число: '))
list_number = fun.get_list(number)
print('Исходный список:\n', list_number)
len_num = len(list_number) // 2 + len(list_number) % 2
l_1, l_2 = list_number[:len_num], list_number[-1:len_num-2:-1]
list_result = list(x*y for x, y in zip(l_1, l_2))
print('Список произведений пар чисел:\n', list_result)