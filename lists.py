# my_list = [1,2,3,4,5]

#Доступ к элементам списка:

# print(my_list[0])
# print(my_list[4])
# print(my_list)


# names = ["Вася", "Людмила", "Степан"]
# print(names[0])
# # #Изменить элемент списка
# names[0] = "Вова"
# print(names)


# Сделайте список, в который добавьте информацию о персонаже
# какой-то игры (Данные можно придумывать) в формате
# Имя, главная способность/особенность/из какой игры, ХП

# Затем выведите данные в формате:

# Имя персонажа: ...
# Главная способность: ....
# Хп персонажа: ....


# character = ["Макс Пейн", "Замедление времени", 100]
# print("Имя персонажа: ", character[0])
# print("Способность персонажа: ", character[1])
# print("ХП персонажа: ", character[2])


# Пример
# my_list1 = [2025, "Год Змеи", True, 5.5]
# print("Сейчас", my_list1[0], "год")


# empty_list1 = list()
# empty_list = []
#
# # Добавить элемент в конец списка:
# empty_list.append(1)
# empty_list.append("aaaaa")
# print(empty_list)

# 1. Создайте список
# с пассажирами самолета, включающий три любых имени.
# 2. Добавьте еще двоих пассажиров в созданный список
# 3. Замените второго пассажира на другого

# 1. ['Вася', "Петя", "Лида"] ->
# 2. ['Вася', "Петя", "Лида", "Женя", "Артем"] ->
# 3. ['Вася', "Вероника", "Лида", "Женя", "Артем"]

#Изменить элемент списка
#имя_списка[0] = на_что_меняем
#Добавить элемент
#имя_списка.append(что_добавляем)

# passengers = ['Вася', "Петя", "Лида"]
# passengers.append("Женя")
# passengers.append("Артем")
# print(passengers)
# passengers[1] = "Вероника"
# print(passengers)

#Склеить списки между собой

# names1 = ["Игорь, Вася"]
# names2 = ["Света", "Лида"]
# names = names1 + names2
# print(names)


# Удалить элемент из списка

# my_list = [1, 2, 3, "abc", 4, 5, 6]
# my_list.remove("abc")
# my_list.remove(1)
# print(my_list)

# Сортировка списка

# my_list = [7,3,10,1,5]
# my_sorted_list = sorted(my_list)
# print(my_sorted_list)

#"Перевернуть" список
# my_sorted_list.reverse()
# print(my_sorted_list)

# Узнать длину списка

# my_list = [7,3,10,1,5]
# print(len(my_list))


# Написать консольное приложение, в котором есть три функции:
# 1. Добавить продукт в список
# 2. Удалить продукт из списка
# 3. Посмотреть список продуктов
# Это должно работать в цикле


# Определим пустой список

# product_list = []
#
# # Функция для добавление элемента в список
# def add_to_list(product):
#     product_list.append(product)
#
# # Функция для удаления элемента из списка
# def remove_from_list(product):
#     product_list.remove(product)
#
# # Переменная для работы цикла
# a = ""
#
# while a != "нет":
#     user_action = input("Добавить (+)/ Удалить (-) или показать весь список (1)?: ")
#     if user_action == "+":
#         product = input("Название продукта для добавления: ")
#         add_to_list(product)
#     elif user_action == "-":
#         product = input("Название продукта для удаления: ")
#         remove_from_list(product)
#     elif user_action == "1":
#         print(product_list)
#     else:
#         print("Неизвестное действие")
#     a = input("продолжим?")


# Перебор элементов списка

# names = ["Артем", "Василий", "Света", "Алиса"]
#
# for name in names:
#     print("Имя в списке: " + name)



# min, max, sum

# numbers = [1, 5, 15, 40, -3, -10, -35]
#
# print("Минимальное значение списка: ", min(numbers))
# print("Максимальное значение списка: ",  max(numbers))
# print("Сумма элементов списка", sum(numbers))



# list1 = [1,2,3]
# list2 = [1,2,3]
# list3 = [5,6,7]
#
# #Сравнение списков
# if list1 == list3:
#     print("Списки одинаковые")
# else:
#     print("Разные списки")


#Срез списка

# some_list = [1, 5, 15, 40, -3, -10, -35]
#
#
# print("Первые три элемента: ", some_list[:3])
# print("Последние три элемента", some_list[4:7])
# print("Взять элементы с шагом 2", some_list[0:7:2])




# test_list = [1, 15 ,4, -6, 0, 10, 25]
#
# #1. Возьмите первые 5 элементов (1 - 0)
#
# print(test_list[0:5])
#
# #2. Возьмите последние два элемента (10, 25)
#
# print(test_list[5:7])
#
# #3. Возьмите элементы (15 - 10) с шагом 3
# print(test_list[1:6:3])
#




# Задача: скопировать себе подсказки:

# Создать список
# my_list = [] либо my_list = [1,2,3,4,....]
#
# my_list.append(элемент) #Добавить элемент
# my_list.remove(элемент)  #Удалить элемент
# my_list[индекс_элемента] = элемент #Заменить элемент
# sorted(название_списка) #Сортировать элементы списка
# название_списка.reverse() #Перевернуть список
# print(len(название_списка)) #Вывести длину списка
#
#
# # Перебрать элементы списка
#
# names = ["Артем", "Василий", "Света", "Алиса"]
#
# for name in names:
#     print("Имя в списке: " + name)
#
# min(), max(), sum() #Самый маленький, большой элемент списка и сумма элементов
#






# 1. Составьте программу по добавлению/удалению дел в список, работающую в цикле
# 2. Пусть программа автоматически сортирует список по алфавиту
# 3. Пусть по команде программа выводит все дела в таком виде:

# - Постирать носки
# - Приготовить еду
# - Попрограммировать на питоне

# 4. Пусть программа выводит количество дел

#
# todo_list = []
#
# def add_to_list(item):
#     todo_list.append(item)
#
# def delete_from_list(item):
#     if todo_list:
#         todo_list.remove(item)
#     else:
#         print("Список пуст")
#
# def watch_list():
#     if todo_list:
#         for item in sorted(todo_list):
#             print("- ", item)
#     else:
#         print("Список пуст")
#
#
#
# usr_action = input("Продолжаем работу со списком? Y/N")
#
# while usr_action == "Y":
#     print("Текущее количество дел: ", len(todo_list))
#     print("1. Посмотреть список")
#     print("2. Добавить дело в список")
#     print("3. Удалить дело из списка")
#     action = input("Какое действие будем делать? ")
#
#     if action == "1":
#         watch_list()
#
#     if action == "2":
#         item = input("Какое дело добавим? ")
#         add_to_list(item)
#
#     if action == "3":
#         item = input("Какое дело удалим из списка? ")
#         delete_from_list(item)
#
#     usr_action = input("Продолжаем работу со списком? Y/N")


















# Создайте два списка:

# Один хранит продукты products в магазине. Например, яблоки, бананы, картофель
# А другой их количество prod_count

# Пусть пользователь сможет добавить новый продукт в список продуктов, а также прописать его цену.

# Пусть в программе будет проверка на то, что продукт закончился. То есть если его количество равно 0, то
# удаляется и продукт из списка.

# Пусть пользователь сможет удалять продукт и его количество самостоятельно.


# products = ["Яблоки", "Бананы", "Картофель"]
# prod_counts = [15, 0, 100]
#
# def add_prod (prod, price):
#     products.append(prod)
#     prod_counts.append(price)
#
# def delete_prod(prod):
#     products.remove(prod)
#
#
# for product, prod_count in zip(products, prod_counts):
#     if prod_count == 0:
#         products.remove(product)
#         prod_counts.remove(prod_count)
# print(products)
# print(prod_counts)
#
#
#



#
# import turtle
# import random
#
# colors = ["red", "blue", "green"]
# while True:
#     turtle.penup()
#     turtle.goto(random.randint(-200,200), random.randint(-200,200))
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.fillcolor(random.choice(colors))
#     turtle.circle(random.randint(-150, 150))
#     turtle.end_fill()
#
# turtle.done()





# my_list = [-1, 0,100, 150, -20, -35, -100, 1000, -250, -300]
# my_list1 = []
#
#
# for i in my_list:
#     if i >= 0:
#         my_list1.append(i)
#
# print(my_list1)





# import turtle
# import random
#
# #Создадим список цветов colors:
# colors = ["red", "green", "blue","yellow", "purple"]
#
# while True:
#     turtle.penup()
#     turtle.goto(random.randint(-200,200), random.randint(-200,200))
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.fillcolor(random.choice(colors))
#
#     rand_or_user = input("Ввести радиус самому (1) или задать рандомно (2) : ")
#     if rand_or_user == "1":
#         radius = int(input("Введи радиус: "))
#     elif rand_or_user == "2":
#         radius = random.randint(50, 100)
#     else:
#         print("Неизвестная команда")
#
#     turtle.circle(radius)
#     turtle.end_fill()
#
# turtle.done()



# my_list1 = [["a","b", "v"], ["а","б","в"]]
#
# print("Буква Б на английском: ",my_list1[0][1])
# print("Буква Б на русском: ",my_list1[1][1])
#
# print("Буква В на английском: ",my_list1[0][2])
# print("Буква В на русском: ",my_list1[1][2])






# users = [["Женя", "password111"], ["Саша", "000010000"]]
#
# def add_user(name, password):
#     temp_list = [name, password]
#     users.append(temp_list)
#
# def delete_user(delete_name, delete_password):
#     for user in users:
#         if user[0] == delete_name and user[1] == delete_password:
#             users.remove(user)
#             break
#         else:
#             print("Такого пользователя не найдено")
#             break
#
#
#
# while True:
#     action = input("Добавить (+) / Удалить (-)? : ")
#     if action == "+":
#         name = input("Введи имя для добавления: ")
#         password = input("Введи пароль пользователя для добавления: ")
#         add_user(name, password)
#     elif action == "-":
#         name = input("Введи имя для удаления: ")
#         password = input("Введи пароль пользователя для удаления: ")
#         delete_user(name, password)
#     elif action == "stop":
#         break
#     else:
#         print("Действие неизвестно")
#
#     print(users)





# 1. Представьте, что вы делаете игру.
# Сделайте список, хранящий имя вашего персонажа, его хп (здоровье) и силу атаки.

# 2. Сделайте еще один список с врагом. Пусть у него, как и у персонажа тоже будет имя, хп
# и сила атаки, а также какой-то уникальный предмет.

# 3. Пусть ваш персонаж атакует врага на величину, равную силе атаки, а враг теряет хп, равное этой величине.
# Сделайте атаку в цикле и завершите его, когда хп врага станет 0 через break, а также укажите количество ходов,
# за которое враг побежден

# 4. Создайте пустой список, который будет хранить предметы вашего персонажа и
# поместите в него уникальный предмет врага, а из его списка удалите этот предмет.

# *Задание со звездочкой*

# 1. Задайте случайное значение силы атаки вашего персонажа, а также ХП врага.
# 2. Сделайте так, чтобы враг также мог атаковать вашего персонажа (у персонажа должно уменьшаться ХП)
# 3. Пусть игрок может активировать специальную способность, которая будет атаковать врага с силой, равной силе атаки * выносливость.
# То есть если сила атаки вашего персонажа будет 20, а выносливость 5, то ХП у врага отнимется 100 единиц.
# Специальную способность можно применить только один раз за игру.


# import random
#
# #1.
# player = ["hero", 100, random.randint(0,10), 3]
#
# #2.
# enemy = ["bad_man", random.randint(5,50), random.randint(0,10), "изумрудный меч"]
#
# objects = []
#
# print(player)
# print(enemy)
#
#
# #3.
# steps = 0
# abilityUsed = False
#
# while True:
#     if enemy[1] <= 0:
#         print("Игрок победил врага за ", steps, " ударов")
#         objects.append(enemy[3])
#         enemy.remove("изумрудный меч")
#         break
#     else:
#         steps += 1
#         print("Удар ", steps)
#         if player[1] > 0:
#             player[1] = player[1] - enemy[2]
#             if abilityUsed == False:
#                 ability = input("Использовать спец.способность сейчас? Y/N")
#                 if ability == "Y":
#                     enemy[1] = enemy[1] - (player[2] * player[3])
#                     abilityUse = True
#                 else:
#                     enemy[1] = enemy[1] - player[2]
#         else:
#             print("Враг победил игрока за ", steps, " ударов")
#             break
#
# print(player)
# print(enemy)
# print(objects)



# import turtle
# import random
#
# t = turtle.Turtle()
# s = turtle.Screen()
#
# s.bgcolor("black")
# t.pencolor("purple")
# t.speed(100)
#
# colors = ["#7FFFD4", "#00BFFF", "#00FFFF", "#00CED1"]
#
# for n in range(5):
#     for x in range(8):
#         for i in range(2):
#             t.pensize(2)
#             t.circle(80+n*20, 90)
#             t.lt(90)
#         t.lt(45)
#     t.pencolor(random.choice(colors))
# s.exitonclick()














































































































