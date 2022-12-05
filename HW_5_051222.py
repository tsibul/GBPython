def something_input(in_type, wellcome_text):
    input_str = input(f'{wellcome_text} : ')
    if in_type == 'int':
        result = int(input_str)
    elif in_type == 'float':
        result = float(input_str)
    else:
        result = input_str
    return result




quit()

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
