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

def split_string(string):
    string = string.replace('+', ' + ')
    string = string.replace('-', ' - ')
    string = string.replace('*', ' * ')
    string = string.replace('/', ' / ')
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')
    return string.split()

def calc_parse(digit_lst):
    new_list = []
    for i in range(len(digit_lst)):
        if digit_lst[i] != '+' and digit_lst[i] != '-' and digit_lst[i] != '*' and digit_lst[i] != '/' and \
            digit_lst[i] != ')' and digit_lst[i] != '(' and i > 0:
            digit_lst[i] = float(digit_lst[i])
            if digit_lst[i-1] == '+':
                new_list.append(digit_lst[i])
            elif digit_lst[i-1] == '-':
                new_list.append(digit_lst[i] * -1)
            elif digit_lst[i-1] == '*':
                new_list[-1] = digit_lst[i] * new_list[-1]
            elif digit_lst[i-1] == '/':
                new_list[-1] = new_list[-1] / digit_lst[i]
        elif digit_lst[i] != '+' and digit_lst[i] != '-' and digit_lst[i] != '*' and digit_lst[i] != '/' and \
                digit_lst[i] != ')' and digit_lst[i] != '(' and i == 0:
            digit_lst[i] = float(digit_lst[i])
            new_list.append(digit_lst[i])
    return sum(new_list)
