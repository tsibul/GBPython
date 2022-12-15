# функции правок

# import controller

# lst для проверки кода
# list_my = [['surname' , 'name', 'phone' , 'notes'], ['surname2' , 'name2', 'phone2' , 'notes2'], ['surname3' , 'name3', 'phone3' , 'notes3']]


def edit(index, arr):
    red_lst = ' '.join(map(str,arr[index])) # парс вложенного листа в строку
    menu_view = f'''Что вы хотите сделать с записью? :
    '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'
    {red_lst}
    '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'
    0 - удалить
    1 - редактировать
    2 - выйти в главное меню
    ввод: '''
    user_answer = edit_question(menu_view)
    if user_answer == 0: # удаление
        new_arr = delete_row(index, arr)
    elif user_answer == 1: # редактирование
        new_arr = update_row(index, arr)
    elif user_answer == 2:
        print_menu # нужно согласовать
    else:
        print('УПС! Некорректный ввод!')
        edit(index, arr)
    
    return new_arr
    

def edit_question(menu_view):
    user_choice = int(input(menu_view))
    return user_choice


def delete_row(index, arr):
    print('Вы собираетесь удалить: \n', ' '.join(map(str,arr[index])))
    user_in = int(input('''Вы действительно хотите удалить?: 
    0 - нет
    1 - да
    ввод: '''))
    if user_in == 0:
        edit(index, arr)
    elif user_in == 1:
        print('Запись удалена')
        del arr[index]
        return arr
    else:
        print('Некорректный ввод!')
        edit(index, arr)

def update_row(index, arr):
    print('Вы редактируете запись: \n', ' '.join(map(str,arr[index])))
    print('''Фамилия, Имя, телефон, адрес
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ введите через пробел''')
    sub_lst = input('→ ').split()
    del arr[index]
    arr.insert(index, sub_lst)
    return arr
    
print(list_my)
new_list = edit(1, list_my)
print(new_list)
