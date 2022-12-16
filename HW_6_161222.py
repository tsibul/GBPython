from My_lib import something_input as s_input
from My_lib import random_list as r_list
from My_lib import split_string
from My_lib import calc_parse
'''
2* Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;'''

string = '7.0-8+3.5*4+1+23*3'
digit_lst = split_string(string)
print(calc_parse(digit_lst))

string2 = '(7*(8+3))*5+1+(1+23)*3'
count = 0
count_prev = 0

while '(' in string2:
    string3 = string2
    for i in range(len(string2)):
        if string2[i] == '(':
            count += 1
            begin = i
        elif string2[i] == ')':
            count -= 1
            end = i
            digit_lst2 = split_string(string2[begin+1:end])
            string3 = string3.replace(string2[begin:end+1], str(calc_parse(digit_lst2)))
    string2 = string3
digit_lst3 = split_string(string2)
print(calc_parse(digit_lst3))

quit()


# =) Все, что ниже показывает как можно воткнуть map, enumerate, lambda куда угодно по делу и без дела

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

float_array = [1, -1.2, 3.1, 5, 10.01]

new_array = list(map(lambda x: abs(x) - round(abs(x), 0), float_array))
max_arr = max(new_array)
min_arr = min(filter(lambda x: x != 0, new_array))

print(f'difference in decimal part {max_arr - min_arr}')

'''
dec_min = find_decimal(float_array[0])
dec_max = find_decimal(float_array[0])
for item in float_array:
    if find_decimal(item) > dec_max:
        dec_max = find_decimal(item)
    elif find_decimal(item) < dec_min and find_decimal(item) != 0:
        dec_min = find_decimal(item)
print(f'difference in decimal part {dec_max - dec_min}')
'''


def dict_from_exp_en(expression):
    exp_split = expression.split(' ')
    exp_split = exp_split[1: -2]
    newexp = list(map(lambda x: x.split('*x^'), exp_split))
    pol_dict = {}
    for item in enumerate(newexp):
        if item[1] == ['+']:
            try:
                key = int(newexp[item[0] + 1][1])
            except:
                key = 0
            value = int(newexp[item[0] + 1][0])
            pol_dict.update({key: value})
        elif item[1] == ['-']:
            try:
                key = int(newexp[item[0] + 1][1])
            except:
                key = 0
            value = - 1 * int(newexp[item[0] + 1][0])
            pol_dict.update({key: value})
    return pol_dict



with open('polynom1.txt', 'rt') as pol1_file:
    pol1_exp = pol1_file.readline()
pol1 = dict_from_exp_en(pol1_exp)


'''
def dict_from_exp(expression):
    exp_split = expression.split(' ')
    exp_split = exp_split[1: -2]
    pol_dict = {}
    for i in range(0, len(exp_split), 2):
        value = int(exp_split[i] + exp_split[i + 1].split('*x^')[0])
        try:
            key = int((exp_split[i + 1].split('*x^'))[1])
        except:
            key = 0
        pol_dict.update({key: value})
    return pol_dict

'''
def get_polynom_en(coeff_arr):
    polynom = ''
    for item in enumerate(coeff_arr):
        if item[0] == 0:
            str_item = ''
        else:
            str_item = '*x^' + str(item[0])
        if item[1] > 0:
            polynom = ' + ' + str(abs(item[1])) + str_item + polynom
        elif item[1] < 0:
            polynom = ' - ' + str(abs(item[1])) + str_item + polynom
    polynom += ' = 0'
    return polynom


pol_power = s_input('int', 'input power (k): ')
pol_range = s_input('int', 'input coeff range: ')
coeff_arr1 = r_list(pol_power + 1, pol_range)
polynom1_exp = get_polynom_en(coeff_arr1)
with open('polynom1.txt', 'wt+') as pol_file:
    pol_file.write(polynom1_exp)

''' Поскольку коэффициенты рандомные поменял порядок (индекс соответствует показателю, в предыдущем варианте было наоборот) 
def get_polynom(coeff_arr):
    polynom = ''
    for i in range(0, len(coeff_arr) - 1):
        if coeff_arr[i] > 0:
            polynom += ' + ' + str(abs(coeff_arr[i])) + '*x^' + str(len(coeff_arr) - i - 1)
        elif coeff_arr[i] < 0:
            polynom += ' - ' + str(abs(coeff_arr[i])) + '*x^' + str(len(coeff_arr) - i - 1)
    if coeff_arr[-1] > 0:
        polynom += ' + ' + str(abs(coeff_arr[-1]))
    elif coeff_arr[-1] < 0:
            polynom += ' - ' + str(abs(coeff_arr[-1]))
    polynom += ' = 0'
    return polynom
'''

def decompress_rle_en(in_file, out_file):
    with open(in_file, 'rt') as inp_file:
        code = inp_file.readline()
    result1 = list(filter(lambda x: x.isdigit(), code))
    result2 = list(filter(lambda x: not x.isdigit(), code))
    len_code = len(result1)
    result = ''
    for i in range(len_code):
        result += result2[i] * int(result1[i])
    with open(out_file, 'wt+') as outp_file:
        outp_file.write(result)

decompress_rle_en('hw5_2_out.txt', 'hw5_2_out2.txt')

''' Старый вариант (правда там был некорректный механизм кодирования, который позволял иметь двухзначный индекс
в новом с двухзначным индексом работать не будет) 
def decompress_rle(in_file, out_file):
    with open(in_file, 'rt') as inp_file:
        code = inp_file.readline()
    result = ''
    for i in range(len(code)):
        coeff = ''
        if not code[i].isdigit():
            j = i
            while code[j - 1].isdigit():
                coeff = code[j - 1] + coeff
                j -= 1
            result = result + int(coeff) * code[i]
    with open(out_file, 'wt+') as outp_file:
        outp_file.write(result)
'''