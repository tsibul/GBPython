import random

def something_input(in_type, wellcome_text):
    input_str = input(f'{wellcome_text} : ')
    if in_type == 'int':
        result = int(input_str)
    elif in_type == 'float':
        result = float(input_str)
    else:
        result = input_str
    return result


def print_task_no(no):
    print('\n')
    print(f'task {no}')


def random_list(length, max_num):
    lst = []
    for i in range(length):
        lst.append(random.randint(- max_num, max_num + 1))
    return lst

def find_decimal(num):
    num_abs = abs(num)
    dec = num_abs - round(num_abs, 0)
    return dec

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


print_task_no(5)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def to_directions_fibonacci(num):
    fib = {-2: -1, -1: 1, 0: 0, 1: 1}
    i = 2
    while i <= num:
        fib.update({i: fib[i-2] + fib[i-1]})
        fib.update({-i: fib[-i+2] - fib[-i+1]})
        i += 1
    return fib


fib_len = something_input('int', 'Input fib length')
arr = dict(sorted(to_directions_fibonacci(fib_len).items()))
print(arr.values())


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print_task_no(4)
number_dec = something_input('int', 'input number: ')
temp_number = number_dec
number_bin = ''
while temp_number > 0:
    number_bin = str(temp_number % 2) + number_bin
    temp_number //= 2
print(number_bin)
# number_bin is string !!!!

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

print_task_no(3)
float_array = [1, -1.2, 3.1, 5, 10.01]
dec_min = find_decimal(float_array[0])
dec_max = find_decimal(float_array[0])
for item in float_array:
    if find_decimal(item) > dec_max:
        dec_max = find_decimal(item)
    elif find_decimal(item) < dec_min and find_decimal(item) != 0:
        dec_min = find_decimal(item)
print(f'difference in decimal part {dec_max - dec_min}')

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
print_task_no('1, 2')
arr_len = something_input('int', 'Input list length:')
item_max = something_input('int', 'Input max of element:')
array = random_list(arr_len, item_max)
result = 0
for i in range(1, arr_len, 2):
    result += array[i]
print(array)
print(f'sum of odd elements: {result}')

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
#последний элемент, второй и предпоследний и т.д

print()
half_len = arr_len // 2 + arr_len % 2
i = 0
mult_pair_list = []
while i < half_len:
    mult_pair_list.append(array[i] * array[-i-1])
    i += 1
print(f'list of pair multiplication {mult_pair_list}')

