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

#array = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},\
#         {"key2": "value2"}]
#array_new = []
#for item in array:
#    if item not in array_new:
#        array_new.append(item)
#print(array)
#print(array_new)

'''
with open('l5_1.txt', 'rt') as inp_file:
    array = list(map(int, inp_file.readline().split()))
print(array)
for i in range(len(array) - 1):
    if array[i] + 1 != array[i + 1]:
        print(array[i] + 1)
'''
# Используем filter
#2. Напишите программу, удаляющую из текста все слова, содержащие "абв"

'''
with open('l5_2.txt', 'rt') as inp_file:
    array2 = list(inp_file.readline().split())
print(array2)
arr = filter(lambda x: 'abv' not in x.lower(), array2)
print(*arr)
'''

#3. Дан список чисел. Создайте список, в который попадают числа, описываемые
#  возрастающую последовательность. Порядок элементов менять нельзя.
#    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


array = [1, 5, 2, 3, 4, 9, 6, 1, 6, 7, 8, 10, 10]

length = len(array)
spread_collection = {}
for i in range(length):
    spread_collection.update({i: [[array[i]]]})

print(spread_collection)

for i in range(length):
    tmp_item = spread_collection[i]
    tmp_small_item = []
    for small_item in tmp_item:
        for j in range(i + 1, length):
            if array[j] > small_item[-1]:
                tmp_small_item = small_item.copy()
                tmp_small_item.append(array[j])
                spread_collection[j].append(tmp_small_item)

tmp_length = 0
for v in spread_collection:
    print(v, spread_collection[v])
    for item in spread_collection[v]:
        if len(item) > tmp_length:
            tmp_arr = [item]
            tmp_length = len(item)
        elif len(item) == tmp_length:
            tmp_arr.append(item)
print(tmp_length)
print(tmp_arr)



