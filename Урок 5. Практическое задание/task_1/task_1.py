"""
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file1 = open('файл2.txt', 'w')
line = input('Введите текст \n')
while line:
    file1.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

