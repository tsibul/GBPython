# ar = [['Фамилия', 'Имя', 'Телефон', 'Комментарий'], ['Иванов', 'Иван', '79854234245', 'Основной'], ['Петров', 'Пётр', '79854237463', 'Основной']]



def show_all(arr):
    print('Вывод всего списка')
    for i in range(len(arr)):
        print(*arr[i])


def show_by_index(arr, index):
    print(f'Телефон под номером {index}:')
    print(*arr[0])
    print(*arr[index])


def show_by_filter(arr, stri):
    substring = str(stri)
    for i in range(1, len(arr)):
        for n in range(len(arr[i])):
            # print(arr[i][n])
            if arr[i][n].find(substring) > -1:
                print(*arr[i])
            
            
def print_menu():
    print('Введите номер команды:', 
    '\n 1: Ввод',
    '\n 2: Редактирование',
    '\n 3: Экспорт',
    '\n 4: Поиск', 
    '\n 5: Удалить', 
    '\n 6: Изменить',
    '\n 7: Выйти')


def menu_search():
    print('Введите номер команды:',
    '\n 1: Вывод всего списка номеров',
    '\n 2: Вывод номера по индексу',
    '\n 3: Поиск номера по имени, фамилии, комментарию') 


# print_menu()
# show_all(ar)
# print()
# n = int(input(f'Введите индекс нужного вам телефона:'))
# show_by_index(ar, n)
# print()
# m = input(f'Введите стоку в поиск: ')
# show_by_filter(ar, m)

