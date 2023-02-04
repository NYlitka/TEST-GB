

def zadacha1():
# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

    N = int(input("введите натуральное число: "))
    result=[]
    for i in range(2,N):
        while N % i == 0:
            result.append(i)
            N //= i
    print (result)

zadacha1()

def zadacha2():

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»


    data=open('ISE.txt',mode='r',encoding='utf-8')
    list= data.readlines()
    data.close()
    n1=set(list[0].removeprefix('\n').split(', '))
    n2=set(list[1].removeprefix('\n').split(', '))
  
    result = n1.difference(n2)
    print (f'Закончилось : {result}')

zadacha2()

import math
def zadacha3():

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142
    N = int(input("введите число: "))
    print(round(math.pi, N))


zadacha3()

