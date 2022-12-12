import ui_c
from calculations import sum_c, sub_c, mult_c, div_c


def check_action(func):
    if func[1] == '+' : return sum_c
    elif func[1] == '-': return sub_c
    elif func[1] == '*': return mult_c
    elif func[1] == '/': return div_c


def check_c(func):
    if func[0].isdigit() and func[2].isdigit():
        return True
    else:
        print("Некорректный ввод")
        return False

