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


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def count_sum_of_digits(input_str):
    count = 0
    for s in input_string:
        if s.isdigit():
            count += int(s)
    print(count)


print_task_no(1)
input_string = something_input('str', 'input float number')
count_sum_of_digits(input_string)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def print_factorials(number):
    temp = 1
    print(temp, end=' ')
    for i in range(2, number + 1):
        temp *= i
        print(temp, end=' ')


print_task_no(2)
input_number = something_input('int', 'input integer number')
print_factorials(input_number)

# 3. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.


def strange_spread(input_number):
    count_sum = 0
    array = []
    for i in range(1, input_number):
        temp = (1 + 1 / i) ** i
        array.append(temp)
        count_sum += temp
    print(array)
    print(count_sum)


print_task_no(3)
strange_spread(input_number)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции вводятся с клавиатуры. 5 2 6


def n_range(length, pos1, pos2):
    array = []
    for i in range(-abs(length), abs(length) + 1):
        array.append(i)
    print(array)
    print(array[pos1] * array[pos2])


print_task_no(3)
input_length = something_input('int', 'input list length')
input_position1 = something_input('int', 'input position 1')
input_position2 = something_input('int', 'input position 2')
n_range(input_length, input_position1, input_position2)

# 5. Реализуйте алгоритм перемешивания списка.


def random_list(length, max):
    lst = []
    for i in range(length):
        lst.append(random.randint(- max, max + 1))
    return lst


def list_mixer(lst):
    lst_len = len(lst)
    index_arr = []
    i = 0
    while (i < lst_len):
        temp = random.randint(0, lst_len-1)
        if temp not in index_arr:
            index_arr.append(temp)
            i += 1
    arr = []
    for j in index_arr:
        arr.append(lst[j])
    return arr


print_task_no(4)
input_length = something_input('int', 'input list length')
input_max = something_input('int', 'input max number')
lst = random_list(input_length, input_max)
print(lst)
print(list_mixer(lst))
