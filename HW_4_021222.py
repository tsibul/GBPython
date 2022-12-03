import random, math


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


def nilakant_element(number):
    sign = 1
    if number / 2 % 2 == 0:
        sign = -1
    element = sign * 4 / (number * (number + 1) * (number + 2))
    return element
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def eratosphen_table(size):
    initial_table = [True] * (size + 1)
    initial_table[0] = False
    initial_table[1] = False
    for i in range(2, size + 1):
        if initial_table[i]:
            j = 2
            while i*j <= size:
                initial_table[i*j] = False
                j = j + 1
    prime_table = []
    for i in range(len(initial_table)):
        if initial_table[i]:
            prime_table.append(i)
    return prime_table

number = something_input('int', 'input number: ')
primes = eratosphen_table(number)
factors = []
for item in primes:
    while number % item == 0:
        number = number / item
        factors.append(item)
print(factors)
check = 1
for smth in factors:
    check *= smth
print(check)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


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


pol_power = something_input('int', 'input power (k): ')
pol_range = something_input('int', 'input coeff range: ')
coeff_arr1 = random_list(pol_power + 1, pol_range)
polynom1_exp = get_polynom(coeff_arr1)
with open('polynom1.txt', 'wt+') as pol_file:
    pol_file.write(polynom1_exp)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# -- первый файл забтраем из предыдущей задачи

pol2_power = something_input('int', 'input power for second polynom (k): ')
pol2_range = something_input('int', 'input coeff for second polynom range: ')
coeff_arr2 = random_list(pol2_power + 1, pol2_range)
polynom2_exp = get_polynom(coeff_arr2)
with open('polynom2.txt', 'wt+') as pol2_file:
    pol2_file.write(polynom2_exp)

with open('polynom1.txt', 'rt') as pol1_file:
    pol1_exp = pol1_file.readline()
with open('polynom2.txt', 'rt') as pol2_file:
    pol2_exp = pol2_file.readline()

pol1 = dict_from_exp(pol1_exp)
pol2 = dict_from_exp(pol2_exp)

coeff_list = []
power_max = max(pol_power, pol2_power)
for i in range(power_max + 1):
    if pol1.get(i) is not None and pol2.get(i) is not None:
        coeff_list.append(pol1.get(i) + pol2.get(i))
    elif pol1.get(i) is not None:
        coeff_list.append(pol1.get(i))
    elif pol2.get(i) is not None:
        coeff_list.append(pol2.get(i))
    else:
        coeff_list.append(0)
coeff_list.reverse()
pol_out = get_polynom(coeff_list)
with open('polynom_out.txt', 'wt+') as polout_file:
    polout_file.write(pol_out)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

print_task_no(2)

arr_len = something_input('int', 'input array length')
arr_max = something_input('int', 'input array max')
array = random_list(arr_len, arr_max)
array_set = set(array)
array_new = []
for item in array:
    if item not in array_new:
        array_new.append(item)
    else:
        array_set.discard(item)
print(array)
print(array_set)



# Вычислить число Pi c заданной точностью d


print_task_no(1)

d_acc = something_input('float', 'input accuracy')
pi_calc_curr = 3
pi_calc_prev = 0
i = 1
while abs(pi_calc_curr - pi_calc_prev) > d_acc:
    pi_calc_prev = pi_calc_curr
    pi_calc_curr += nilakant_element(i * 2)
    i += 1

print(F'calculated PI: {pi_calc_curr} , steps: {i}')
print(F'previous calculated PI: {pi_calc_prev}')
print(F'calculated difference: {abs(pi_calc_curr - pi_calc_prev)}')
print(F'diiference with math.PI:{abs(pi_calc_curr - math.pi)}')

