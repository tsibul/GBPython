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


# 1/ Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def task1():
    print_task_no(1)
    day_number = something_input('int', 'input weekday number')
    message = ' No '
    if 5 < day_number < 8:
        message = ' Yes '
    elif day_number < 1 or day_number > 7:
        message = 'Error '
    print(message)


task1()

# 2/ Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def task2():
    print_task_no(2)
    result = True
    X = [True, False]
    Y = [True, False]
    Z = [True, False]
    for x in X:
        for y in Y:
            for z in Z:
                result = result and (not(x or y or z) == (not x and not y and not z))
    print(result)


task2()


# 3/ Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def task3():
    print_task_no(3)
    x = something_input('float', 'input x')
    y = something_input('float', 'input y')
    if x == 0 or y == 0:
        return print('point is on axis')
    if x > 0 and y > 0:
        return print(f'({x}, {y}) in quater 1')
    if x < 0 and y > 0:
        return print(f'({x}, {y}) in quater 2')
    if x < 0 and y < 0:
        return print(f'({x}, {y}) in quater 3')
    print(f'({x}, {y}) in quater 4')


task3()


# 4/ Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def task4():
    print_task_no(4)
    quater_no = something_input('str', 'input quater no')
    if quater_no == '1':
        return print('0 < X < oo , 0 < Y < oo')
    elif quater_no == '2':
        return print('-oo < X < 0 , 0 < Y < oo')
    elif quater_no == '3':
        return print('-oo < X < 0 , -oo < Y < 0')
    elif quater_no == '4':
        return print('0 < X < oo , -oo < Y < 0')
    else:
        print('not correct quater')


task4()


# 5/ Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.


def task5():
    print_task_no(5)
    x1 = something_input('float', 'input x1')
    y1 = something_input('float', 'input y1')
    x2 = something_input('float', 'input x2')
    y2 = something_input('float', 'input y2')
    distance = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 3)
    print(f'distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}')


task5()

