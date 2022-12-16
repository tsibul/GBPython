# backend user menu + check call the menu
from outputs import print_menu

menu = \
    {
        '1': 'Ввод', 
        '2': 'Редактирование', 
        '3': 'Экспорт', 
        '4': 'Поиск', 
        '5': 'Удалить', 
        '6': 'Изменить', 
        '7': 'Выйти'
    }

def change_menu_position(string, len_menu = 7): # можно передовать длину словаря для масштабирования
    if string.isdigit() == True:
        digit = int(string) 
        if digit > 0 and digit <= len_menu:
            return str(string)
        else:
            print('Некорректный ввод!')
            print_menu()
    else:
        print('Некорректный ввод!23')
        print_menu()
