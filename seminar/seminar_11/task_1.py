# Написать функцию thesaurus_adv(), принимающую в 
# качестве аргументов строки в формате 
# «Имя Фамилия» и возвращающую словарь, в котором 
# ключи — первые буквы фамилий, а 
# значения — словари, реализованные по схеме 
# предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы. 
# Например: >>> thesaurus_adv
# ("Иван Сергеев", "Инна Серова", "Петр Алексеев", 
# "Илья Иванов", "Анна Савельева") 
# { "А": { "П": ["Петр Алексеев"] }, 
# "И": { "И": ["Илья Иванов"] }, 
# "С": { "И": ["Иван Сергеев", "Инна Серова"], 
# "А": ["Анна Савельева"] } }

str_input = "Иван Сергеев"
lst_input = []
dict_1 = {}
dict_2 = {}
str_sort = ''
for i in str_input:
    if i.isupper():
        str_sort += i
lst_input.append(str_input)
dict_1[str_sort[0]] = lst_input
dict_2[str_sort[1]] = dict_1 

str_input = "Петр Алексеев"
lst_input = []
dict_1 = {}
# dict_2 = {}
str_sort = ''
for i in str_input:
    if i.isupper():
        str_sort += i
lst_input.append(str_input)
dict_1[str_sort[0]] = lst_input
dict_2[str_sort[1]] = dict_1 

str_input = "Инна Серова"
lst_input = []
dict_1 = {}
# dict_2 = {}
str_sort = ''
for i in str_input:
    if i.isupper():
        str_sort += i
lst_input.append(str_input)
dict_1[str_sort[0]] = lst_input
dict_2[str_sort[1]] = dict_1 

print(dict_2)