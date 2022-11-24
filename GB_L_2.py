# https://pastebin.com/Vxhwh8Qw 12345


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


# Для N = 5: 1, -3, 9, -27, 81

# print_task_no(1)
# n = something_input('int', 'input number N')
# for i in range(1, n + 1):
#     if i % 2:
#         print(3 ** (i - 1), end=', ')
#     else:
#         print(- 3 ** (i - 1), end=', ')

# 3n+1

#print_task_no(2)
#array = []
#for i in range(n + 1):
#    array.append(3 * i + 1)
#print(array)


print_task_no(3)
str1 = something_input('str', 'input number string 1')
str2 = something_input('str', 'input number string 2')
if len(str1) > len(str2):
    str1, str2 = str2, str1
length = len(str1)
count = 0
for i in range(len(str2) - length + 1):
    tmp = []
    for j in range(length):
        tmp.append(str2[j + i])
    if str1 == ''.join(tmp):
        count += 1
print(count)
