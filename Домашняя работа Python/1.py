# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

# names = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресение"]
# x = int(input("Введите число"))
# x -= 1
# if x < 7 and x >= 0:
#     print(names[x])
# else:
#     print("Такого дня недели нет")

   

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# def inputNumbers(x):
#     xy = ["X", "Y"]
#     a = []
#     for i in range(x):
#         is_OK = FalseG
#         while not is_OK:
#             try:
#                 number = int(input(f"Введите координату по {xy[i]}: "))
#                 a.append(number)
#                 is_OK = True
#             except ValueError:
#                 print(" Вводить надо целые числа!")
#     return a


# def calculateLengthSegment(a, b):
#     lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return lengthSegment


# print("Введите координаты точки А")
# pointA = inputNumbers(2)
# print("Введите координаты точки В")
# pointB = inputNumbers(2)

# print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")



# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0


# def what_coordinates(number):
#     if number == 1:
#         return f'В {number} четверти координаты точки по оси X могут быть в диапазоне (0, + ∞) и Y (0, + ∞)'
#     elif number == 2:
#         return f'Во {number} четверти координаты точки по оси X могут быть в диапазоне (0, - ∞) и Y (0, + ∞)'
#     elif number == 3:
#         return f'В {number} четверти координаты точки по оси X могут быть в диапазоне (0, - ∞) и Y (0, - ∞)'
#     elif number == 4:
#         return f'В {number} четверти координаты точки по оси X могут быть в диапазоне (0, + ∞) и Y (0, - ∞)'
#     else:
#         return 'Неверный номер четверти'

# quarter = int(input('Введите номер четверти от 1 до 4: '))
# print(what_coordinates(quarter))



# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8


def addNumbers():
    print ("Введите число")
    number = int (input())
    N=0
    while number > N+1:
        N=N+2
        print (N,end=" ")
    

addNumbers()





