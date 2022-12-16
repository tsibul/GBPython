

quit()


def decompress_rle_en(in_file, out_file):
    with open(in_file, 'rt') as inp_file:
        code = inp_file.readline()
    result1 = list(filter(lambda x: x.isdigit(), code))
    result2 = list(filter(lambda x: not x.isdigit(), code))
    len_code = len(result1)
    result = ''
    for i in range(len_code):
        result += result2[i] * int(result1[i])
    with open(out_file, 'wt+') as outp_file:
        outp_file.write(result)

decompress_rle_en('hw5_2_out.txt', 'hw5_2_out2.txt')

''' Старый вариант (правда там был некорректный механизм кодирования, который позволял иметь двухзначный индекс
в новом с двухзначным индексом работать не будет) 
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
'''