# def zadacha1():
# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8


    # fib1 = 0
    # fib2 = 1
    # n = int(input('Введите число \n'))
    # 
    # data=open('fibonachi.txt',mode='w',encoding='utf-8')
    # for i in range(n):
    #     data.write (str(fib2)+'\n')
    #     fib1, fib2 = fib2, fib1 + fib2
    #     
    #     print (fib1, end=' ')
    # data.close
# def zadacha1()


# def zadacha2():
#     # Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
#     # а –> абрикос, авокадо, апельсин, айва.
#     # def zadacha2 ():
#     data = open('fruits.txt', encoding='utf-8')
#     fruittext = data.readlines()[0].split (' ')
#     data.close()
#     print (fruittext)

#     litter = input ('Введите букву:\n')

#     for fruit in fruittext:
#         if fruit[0]== litter:
#             print (fruit)
# zadacha2()           


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
#  отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

# def zadacha3():
text_dictionary = \
{   
    'привет': 'здравствуй',
    'как дела': 'норм',
    'как тебя зовут': 'Алекса'
}

# startdialog = True

# while startdialog:
#     text = input('Я: ')
#     text = text.lower()
#     if text in text_dictionary.keys():
#         print (f'Бот: {text_dictionary[text]}')
#     else:
#         print (f'Бот: Не понял....')
    
#     if text == 'выход' or text == 'пока' :
#         startdialog = False

