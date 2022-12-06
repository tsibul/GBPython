import random, os


def something_input(in_type, wellcome_text):
    input_str = input(f'{wellcome_text} : ')
    if in_type == 'int':
        result = int(input_str)
    elif in_type == 'float':
        result = float(input_str)
    else:
        result = input_str
    return result


# Создайте программу для игры в ""Крестики-нолики"".

def print_board(field):
    hor_divider = '+---' * 3 + '+'
    for i in range(0, 9, 3):
        j = i
        hor_line = ''
        while j < i + 3:
            hor_line += '| ' + field[j] + ' '
            j += 1
        hor_line += '|'
        print(hor_divider)
        print(hor_line)
    print(hor_divider)

def move(sign, field):
    print(f'turn {sign}')
    row = 0
    while (row < 1 or row > 3) or ' ' not in field[row * 3 - 3: row * 3]:
        row = something_input('int', 'input row number (from top)')
    pos = 0
    while pos < 1 or pos > 3 or field[row * 3 - 3 + pos - 1] != ' ':
        pos = something_input('int', 'input position number (from left)')
    field[row * 3 - 4 + pos] = sign


def check_result(field):
    for i in range(3):
        if field[i * 3] == field[i * 3 + 1] == field[i * 3 + 2] and field[i * 3] != ' ':
            return field[i * 3]
        elif field[i] == field[i + 3] == field[i + 6] and field[i] != ' ':
            return field[i]
        elif (field[0] == field[4] == field[8] or field[2] == field[4] == field[6]) and field[4] != ' ':
            return field[4]
    return None


def xo_gameflow():
    field = [' '] * 9
    turn = 'X'
    chck = None
    print_board(field)
    while chck is None and ' ' in field:
        move(turn, field)
        print_board(field)
        chck = check_result(field)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    end_game = 'deuce'
    if chck is not None:
        end_game = chck + ' WIN!'
    print(end_game)


xo_gameflow()
quit()

#Создайте программу для игры с конфетами человек против человека.


def game_mode():
    no_players = 0
    no_take = 0
    no_sweets = 0
    while no_players < 1 or no_players > 2:
        no_players = something_input('int', 'input number of players (1 or 2)')
    while no_take < 2 or no_take > 40:
        no_take = something_input('int', 'input number of sweets you can take (from 2 to 40)')
    while no_sweets <= no_take:
        no_sweets = something_input('int', 'input  total number of sweets ore than ' + str(no_take))
    return no_players, no_take, no_sweets


def input_names(game_mode):
    name1 = 'Artificial_Brain'
    while name1 == 'Artificial_Brain':
        name1 = something_input('str', 'input name of first player: ')
    if game_mode == 2:
        name2 = something_input('str', 'input name of second player: ')
    else:
        name2 = 'Artificial_Brain'
    if random.randint(1, 1001) % 2 == 0:
        turn = True
        print(f'first turn of {name1}')
        name = name1
    else:
        turn = False
        print(f'first turn of {name2}')
        name = name2
    print()
    return turn, name1, name2, name


def artifitial_brains(sweets, possible_take, no_take):
    if sweets % (no_take + 1) == 0:
        take = random.randint(1, possible_take + 1)
    else:
        take = sweets - sweets // (no_take + 1) * (no_take + 1)
    return take


def game_flow(turn, name1, name2, name, no_take, sweets):
    while sweets > 0:
        print(f'sweets left {sweets}')
        if sweets >= no_take:
            possible_take = no_take
        else:
            possible_take = sweets
        take1 = 0
        while take1 > possible_take or take1 < 1:
            if name != 'Artificial_Brain':
                take1 = something_input('int', name + ' take sweets from 1 to ' + str(possible_take))
            else:
                take1 = artifitial_brains(sweets, possible_take, no_take)
        print(f'{name} takes {take1} sweets')
        sweets -= take1
        if sweets == 0:
            print()
            print(f'{name} win !!!! congrats to {name}')
        if turn:
            name = name2
        else:
            name = name1
        turn = not turn


no_players, no_take, no_sweets = game_mode()
turn, name1, name2, name = input_names(no_players)
game_flow(turn, name1, name2, name, no_take, no_sweets)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# !!! не работает, если символ цифра


def compress_rle(in_file, out_file):
    with open(in_file, 'rt') as inp_file:
        string = inp_file.readline()
    cur_element = string[0]
    i = 0
    j = 0
    code = ''
    while i < len(string) - 1:
        while cur_element == string[i] and i < len(string):
            i += 1
        code += str(i - j) + cur_element
        j = i
        cur_element = string[i]
    with open(out_file, 'wt+') as outp_file:
        outp_file.write(code)


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


compress_rle('hw5_2_in.txt', 'hw5_2_out.txt')
decompress_rle('hw5_2_out.txt', 'hw5_2_out2.txt')


#Напишите программу, удаляющую из текста все слова, содержащие "абв"

with open('l5_2.txt', 'rt') as inp_file:
    array2 = list(inp_file.readline().split())
print(array2)
arr = ' '.join(str(x) for x in list((filter(lambda x: 'abv' not in x.lower(), array2))))
with open('hw5_1.txt' , 'wt+') as out_file:
    out_file.write(arr)
