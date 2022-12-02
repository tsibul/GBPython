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



quit()


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

