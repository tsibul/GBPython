
'''
exports.py
def export_file - спрашивает формат файла 1 - csv, 2 - xml, 3 - html
и вызывает соответствующую функцию	
def export_csv(arr) экспорт в csv файл 
def export_xml(arr) экспорт в xml файл 
def export_html(arr) экспорт в html файл
'''

import os
os.chdir(os.path.dirname(__file__))
from xml.etree import ElementTree as ET


def export_file():# Функция возвращает строчку!
    while True:
        user_input = input(f"Выберите формат экспортируемого файла (введите 1, 2 или 3), где:\n 1 - файл формата 'csv'.\n 2 - файл формата 'xml'. \n 3 - файл формата 'html'.\n Произведите ввод: ")

        if user_input.isdigit() and int(user_input) == 1:
            print("Вы выбрали - 1: экспорт файла в формате csv.")
            break
        elif user_input.isdigit() and int(user_input) == 2:
            print("Вы выбрали - 2: экспорт файла в формате xml.")
            break
        elif user_input.isdigit() and int(user_input) == 3:
            print("Вы выбрали - 3: экспорт файла в формате html.")
            break
        else:
            print("Вы ввели что то не то! Попробуйте щее раз")
    return user_input


def export_csv(arr):
    name_file = input("Введите название файла: ")
    with open(f'{name_file}.csv', 'w', encoding='utf-8') as file:
        for text in arr:
            res_text = ", ".join(text)
            file.writelines(f'{res_text}; \n')
    print(f"Экспорт файла {name_file}.csv завершен.")


def export_xml(arr):
    name_file = input("Введите название файла: ")
    Phone_Book = ET.Element('Phone_Book')
    for item in arr:
        user = ET.SubElement(Phone_Book, f'user')
        surname = ET.SubElement(user, 'surname')
        surname.text = item[0]
        name = ET.SubElement(user, 'name')
        name.text = item[1]
        telephone = ET.SubElement(user, 'telephone')
        telephone.text = item[2]
        comments = ET.SubElement(user, 'comments')
        comments.text = item[3]
    data = ET.tostring(Phone_Book, encoding='unicode')
    file = open(f'{name_file}.xml', 'w', encoding='utf-8')
    file.writelines(data)
    print(f"Экспорт файла {name_file}.xml завершен.")


def export_html(arr):
    name_file = input("Введите название файла: ")
    with open(f'{name_file}.html', 'w', encoding='utf-8') as file:
        file.writelines(f'<!DOCTYPE html>\n')
        file.writelines(f'<html lang="ru">\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\t\t<meta charset="utf-8">\n')
        file.writelines(f'\t\t<title>Phone Book</title>\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\n')
        file.writelines(f'\t<body>\n')
        file.writelines(f'\t\t<h2>Phone Book</h2>\n')
        file.writelines(f'\t\t<table border="1" width="600">\n')
        file.writelines(f'\t\t\t<thead>\n')
        file.writelines(f'\t\t\t<tbody>\n')
        file.writelines(f'\t\t\t\t<tr>\n')
        file.writelines(f'\t\t\t\t\t<th>№</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Фамилия</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Имя</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Телефон</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Комментарий</th>\n')
        file.writelines(f'\t\t\t\t</tr>\n')
        file.writelines(f'\t\t\t</thead>\n')
        count = 1
        for text in arr:
            file.writelines(f'\t\t\t\t<tr>\n')
            file.writelines(f'\t\t\t\t\t<td>{count}</td> \n')
            for item in text:
                file.writelines(f'\t\t\t\t\t<td>{item}</td> \n')
            file.writelines(f'\t\t\t\t</tr>\n')
            count += 1
        file.writelines(f'\t\t\t</tbody>\n')
        file.writelines(f'\t\t</table>\n')
        file.writelines(f'\t</body>\n')
        file.writelines(f'</html>')
            
    print(f"Экспорт файла {name_file}.html завершен.")


user_unput = export_file()

if user_unput == '1':
    export_csv(arr)

elif user_unput == '2':
    export_xml(arr)

else:
    export_html(arr)