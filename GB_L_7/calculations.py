def sum_c(num1, num2):
    rez = num1 + num2
    return rez

def sub_c(num1, num2):
    rez = num1 - num2
    return rez

def mult_c(num1, num2):
    rez = num1 * num2
    return rez

def div_c(num1, num2):
    rez = num1 / num2
    return rez


def calculation(num1, fun, num2):
    return fun(num1, num2)