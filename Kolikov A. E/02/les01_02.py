# coding: utf-8

# Python. Быстрый старт.
# Занятие 2.

# Домашнее задание: в случае, если пользователь ввел Y, то придумать и вывести список действий,
#                    спросить, какое он хочет выполнить;
#                   ознакомиться с PEP8
import os
print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
    
# PEP-8 рекомендует делать отступ, равный 4 пробелам   
if answer == 'Y' or 'y':
    print("Отлично, хозяин!")# <- здесь будет код домашнего задания
    print("Я умею:")
    print(" [1] - сложу два числа")
    print(" [2] - найду счастливое число")
    print(" [3] - показать файлы формата .jpg")
    print(" [4] - выведу имя операционной системы")
    do = int(input("Укажите номер действия: "))
if do == 1:
    a = int(input("Введите число a ="))
    b = int(input("Введите число b ="))
    print(" a + b = ", a + b )
if do == 2:
    n = str(input())
    n = int(n)
    sum1 = n % 10 + (n %100)//10 + (n % 1000)//100
    sum2 = (n // 1000) %10 + (n // 10000) %10 + n // 100000
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
if do == 3:
    files = [f for f in os.listdir() if f.endswith('.jpg')]
    print(files)
if do == 4:
     print(os.name())
# Оператор == (двойное равно) - это логический оператор сравнения
elif answer == 'N' or 'y':    
    print("До свидания!")
else:
    print("Неизвестный ответ")    