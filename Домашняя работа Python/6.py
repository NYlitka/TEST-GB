# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396
def zadacha1():
    N = input('Введите число: ')
    print (int(N*3)+int(N*2)+int(N))

zadacha1()

import random
# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def zadacha2():
    N=[str(random.randint(0,9)) for _ in range(15)]
    print (N)
    enternum = int(input('Введите число: '))
    result = ''
    for el in N:
        result += str(el)
    if str(enternum) in result:
        print ('Есть число')
    else:
        print ('нет такого числа')
        
zadacha2()


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


def numbers(x,y):
    minN = min(x,y)
    devider=1
    for el in range(2,minN+1):#
        if x % el == 0 and y % el==0:
            devider=el
            break
    return devider == 1


def zadacha3():
    for y in range(1,12):
        for x in range(1,y):
            if numbers(x,y):
                print (f'{x}/{y}', end =' ')
        print()

zadacha3()