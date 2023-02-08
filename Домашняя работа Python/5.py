import random
def zadacha1():
# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
    numberlist = list (random.randint(1,10)for _ in range(random.randint(5,12)))
    print(f'список случайных чисел: {numberlist}')
    result=list (filter(lambda x: x > 5, numberlist))
    print (result)

zadacha1()

def zadacha2():

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

    numberlist = list (random.randint(1,100)for _ in range(random.randint(5,12)))
    print(f'список случайных чисел: {numberlist}')
    index= random.randint(0,len(numberlist)-1)
    result =[numberlist[index]]


    while index < len(numberlist):
        index = random.randint(index,len(numberlist))
        if index != len(numberlist) and numberlist[index] > result[-1]:
            result.append (numberlist[index])

    print(result)

zadacha2()

def zadacha3():

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]
    numberlist = list (random.randint(1,10)for _ in range(random.randint(0,120)))
    print(f'список случайных чисел: {numberlist}')

    result = list(filter(lambda x: numberlist.count (x) > 1, numberlist ))
    print(f'список уникальных чисел: {set (numberlist)}')
    result = list(map(lambda x: numberlist.count (x) > 1, numberlist ))
    print(f'количество повторений в списке: {result.count(True)}')



zadacha3()
