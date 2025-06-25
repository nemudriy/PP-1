# Вывод

print(123)
print(1.23)
print("Hello")
print(True)

# Запись/Ввод

word = input("Введи слово ")
print(word)

mass = int(input("Введи массу ")) #Целое число
mass2 = float(input("Введи массу ")) #Дробное число
print(mass2 + 15)


# Условия

print(15>0)
print(15<0)
print(15==15)
print(15!=20)

if проверка:
    действие

number = int(input("Введи число для проверки "))

if number > 0:
    print("Это положительное число")
if number < 0:
    print("Это отрицательное число")
if number == 0:
    print("Это нуль")



number = int(input("Введи число для проверки "))

if number > 0:
    print("Это положительное число")
elif number < 0:
    print("Это отрицательное число")
else:
    print("Это нуль")

name = "Вася"
age = 29

if name == "Вася":
    if age > 30:
        print("Что-то")



# and

# if не идет снег and на улице тепло:
#     Идем гулять
#
# if нет дз на завтра or на улице тепло:
#     Идем гулять


num = 8

if num > 0 and num % 2 == 0:
    print("num - положительное число, делящееся на 2 нацело")

if num > 0 or num % 5 == 0:
    print("num - положительное число или делится на 5 нацело")


# boolean_per = not True
# print(boolean_per)

name = "Вася"

if not name == "admin":
    print("Привет, пользователь")




# Циклы

#Пока что-то истина, выполняем какие-то действия


while True:
    print("Спам!")


i = 0

while i < 5:
    print(i)
    i = i + 1


i = 0

while i < 5:
    i = i + 1
    if i == 3:
        print("Это 3!")
        continue
    print(i)

# Вложенный цикл while

size = 5 #Размер таблицы умножения

i = j = 1

while i <= size:
    while j <= size:
        print(i*j)
        j = j + 1
    print("\n")
    j = 1
    i = i + 1


for i in range(1,8):
    print(i)

for i in "hello, world":
    if i == ",":
        print("Нашел ,")


# Функции и методы

def some_action():
    print("action1")
    print("action2")
    print("action3")

some_action()



import turtle

size = int(input("Введи размер фигуры: "))

def draw_square(size):
    for i in range(0,4):
        turtle.forward(size)
        turtle.left(90)

def draw_circle(size):
    turtle.circle(size)

draw_square(size)
draw_circle(size)

turtle.done()



# Напишите функцию, считающую  координату материальной точки

# Вам известна скорость точки и ее время t. Данные можете собрать с пользователя.
# Создайте функцию, которая вернет произведение скорости и времени.

# Суммируйте результат с начальной координатой (тоже запросите у пользователя)

x = x0 + V * t


x0 = int(input("Введи начальную координату: "))
V = int(input("Введи скорость точки: "))
t = int(input("Введи время: "))

def temp_func(v,t):
    return v*t

print(x0 + temp_func(V,t))












# Пример
def sum(a,b):
    return a+b

print(5*sum(1,10))





login = input("Твой логин: ")
password = input("Твой пароль: ")

def auth(l,p):
    if l == "admin" and p == "12345":
        return True
    elif l== "jeka" and p == "77777":
        return True
    else:
        return False

if auth(login, password) == True:
    print("Добро пожаловать")
else:
    print("Не удалось авторизоваться")








































































































