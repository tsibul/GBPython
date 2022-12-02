import random
import datetime, math





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


def get_rand():
    return datetime.datetime.now().microsecond

#3. Задайте два числа. Напишите программу, которая найдёт НОК
#   (наименьшее общее кратное) этих двух чисел.

# Алгоритм нахождения НОД делением
# Большее число делим на меньшее.
# Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
# Если есть остаток, то большее число заменяем на остаток от деления.
# Переходим к пункту 1.


def f_nod(a_temp, b_temp):
    while a_temp != b_temp:
        if a_temp > b_temp:
            a_temp = a_temp - b_temp
        else:
            b_temp = b_temp - a_temp
    return a_temp


def f_nod_2(a_temp, b_temp):
    if a_temp > b_temp:
        a_temp, b_temp = b_temp, a_temp
    nod = a_temp
    while a_temp % nod != 0 or b_temp % nod != 0:
        nod -= 1
    return nod


num_a = 6
num_b = 4

nok = (num_a * num_b) // f_nod_2(num_a, num_b)

print(f_nod_2(num_a, num_b))
print((num_a * num_b) // f_nod_2(num_a, num_b))

quit()

#2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#    С помощью математических формул нахождения корней квадратного уравнения

a = something_input('int', 'input A')
b = something_input('int', 'input B')
c = something_input('int', 'input C')

print(F'{a}x**2 + {b}x + {c} = 0')

discr = b ** 2 - 4 * a * c
print(f"Дискриминант D = {discr}")

if discr > 0:
    x1 = (-b + (discr**0.5)) / (2 * a)
    x2 = (-b - (discr**0.5)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")

# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.


line = '1, -22, 3, -054, 50, 100, 95'
a_list = line.split(', ')

t_min = int(a_list[0])
t_max = int(a_list[0])
for item in a_list:
    if int(item) < t_min:
        t_min = int(item)
    if int(item) > t_max:
        t_max = int(item)

print(*a_list)
print(f'Min: {t_min}')
print(f'Max: {t_max}')






with open('HW_3_291122.txt', 'r') as t_file:
    print(1, t_file.read())
    print(2, t_file.readline())
    print(3, t_file.readline())
    print(4, t_file.readline())
    print(5, t_file.readlines())


f_file = open('HW_3_291122.txt', 'r')
print(7, f_file.readline())
print(8, f_file.readline())
print(9, f_file.readline())
print(10, f_file.readlines())
f_file.close()

mylist = ['22', '33', '123', 'fwefe', 'ytyy', '55']

print(mylist.index('22'))