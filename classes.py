# class Color:
#     def __init__(self, color_code):
#         self.color_code = color_code
#         print(color_code)
#
#
# yellow = Color("#fbff00")
# white = Color("#ffffff")
# red = Color("#ff0000")



# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#
# car1 = Car("Audi", 1980)
# car1.name = "Ferrari"
# car1.color = "Красный"
#
# car2 = Car("Niva", 2003)
#
#
# print("Марка первой машины:", car1.name)
# print("Год выпуска первой машины:", car1.year)
# print("Цвет первой машины: ", car1.color)
#
# print(vars(car1))
# print(vars(car2))




# Создайте класс одежда, в котором определите параметры: вид одежды, размер и цвет
# Создайте несколько объектов этого класса.
# Со звездочкой* Добавьте еще атрибут цены вне класса

# class Cloth:
#     def __init__(self, type, size, color):
#         self.type = type
#         self.size = size
#         self.color = color
#
# cloth1 = Cloth("Кроссовки", 42, "Белый")
# cloth1.price = 2000
# cloth2 = Cloth("Штаны", 40, "Черный")
# cloth2.price = 5000
# print(vars(cloth1))




# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#     def show_user_info(self):
#         print(f"Имя пользователя : {self.name}, пароль пользователя: {self.password}")
#     def change_password(self, old_password, new_password):
#         if old_password == self.password:
#             self.password = new_password
#             print("Пароль успешно заменен")
#         else:
#             print("Старый пароль неверен")
#
#
# user1 = User("admin", "123455")
# user1.show_user_info()
# user1.change_password("123455", "999999")
# user1.show_user_info()
#



# 1. Вы - разработчик приложений для электронной библиотеки. Поздравляю!!!!
# 2. Вам прилетает задача: сделать приложение для учета книг
# и последующей работы с ними:
# 3. Запросы такие: хранить название книги, год издания, автора
# и тематику (роман, проза, ноука,...)
# 4. Нужна возможность просмотра информации о книге,
# а также возможность поменять любой из параметров.
# 5. Также пусть будет возможность добавить новую книгу (создать новый объект)


# class Book:
#     def __init__(self, name, year, autor, theme):
#         self.name = name
#         self.year = year
#         self.autor = autor
#         self.theme = theme
#
#     def show_book_info(self):
#         print(f"Название книги: {self.name},"
#               f" год издания: {self.year}"
#               f", автор: {self.autor},"
#               f" тематика: {self.theme}")
#
#     def replace_parameter(self, what, new_parameter):
#         if what == "name":
#             self.name = new_parameter
#         elif what == "year":
#             self.year = new_parameter
#         elif what == "autor":
#             self.autor = new_parameter
#         elif what == "theme":
#             self.theme = new_parameter
#         else:
#             print("Такого параметра тут нет")
#
#
# book = Book("Основы академического рисунка", "2020", "Николай Геннадьевич Ли", "Хобби")
# book.show_book_info()
# book.replace_parameter("year", "2021")
# book.show_book_info()




# В класс User добавьте новый метод change_password, в котором определены параметры: self,
# old_password, new_password.
# Внутри этого метода сделайте проверку:
# Если старый пароль пароль совпадает с self.password, то мы  заменяем старый пароль на новый,
# и выводим сообщение об успешном изменении пароля
# Если пароли на совпадают, то говорим об этом в сообщении.

# Проверьте правильность выполнения, вызвав метод show_user_info до смены пароля и после.


# 1. Создаем класс User. В нем будет конструктор, в котором будут параметры name и password
# 2. Добавляем метод show_user_info(), чтобы отобразить данные пользователя
# 3. Добавялем новый метод change_password, в котором будут параметры old_password и new_password
# 3.1 Внутри метода будет проверка: если password == old_password,
# то мы заменим password на new_password
# 3.2. В ином случае заменить пароль нельзя, потому что не совпадают
# 4. Создать объект класса User, потом вызвать метод change_password с параметрами.



class Car:
    def __init__(self, name, speed):
        self.name = name
        self.__speed = speed
    def print_info_car(self):
        print(f"Название машины {self.name}, Максимальная скорость: {self.__speed}")

car1 = Car("Mazda", 150)
car2 = Car("AAA", 150)

cars = [car1, car2]

print(cars[0])
#
# car1.print_info_car()
# car1.name = "Mersedes"
# car1.__speed = -200
# car1.print_info_car()


# Создайте класс Bank, где атрибуты имя и возраст будут изменяемыми,
# а количество денег на счету и кредитный рейтинг закрытыми от изменений.

# Добавьте функцию для просмотра данных о пользователе.

# Самостоятельно добавьте сеттер и геттер для атрибута адреса пользователя

# class Person:
#     def __init__(self, name, age, address):
#         self.__name = name
#         self.__age = age
#         self.__address = address
#
#     def set_age(self, age):
#         if age < 0 or age > 110:
#             print("Недопустимый возраст")
#         else:
#             self.__age = age
#
#     def set_address(self, address):
#         if address:
#             self.__address = address
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_address(self):
#         return self.__address
#
#     def print_person(self):
#         print(f"Имя {person1.get_name()} возраст {person1.get_age()} адресс {person1.get_address()}")
#
# person1 = Person("Василий", 20, "Улица Пушкина дом Колотушкина")
# person1.print_person()
# person1.set_age(30)
# person1.set_address("Улица Пушкина дом 6")
# person1.print_person()
# print(person1.get_name())
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         print("% Получение баланса %")
#         return self.__balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance < 0:
#             print("Значение не может быть отрицательным")
#         else:
#             print("Значение изменено")
#             self.__balance = new_balance
#
# account1 = BankAccount(1000)

# Представьте, что вам нужно сделать механику торговли в игре. Для этого нужно реализовать
# класс Trade и атрибут money (количество денег у игрока)

# Необходимо реализовать методы user_money (геттер и сеттер) для просмотра количества денег у игрока и
# для изменения этого количества при покупке какого-то предмета (можно зарандомить это значение)


# import random
#
# class Trade:
#     def __init__(self, user_money):
#         self.__user_money = user_money
#
#     @property
#     def user_money(self):
#         return self.__user_money
#
#     @user_money.setter
#     def user_money(self, item_cost):
#         temp = self.__user_money - item_cost
#         if temp < 0:
#             print("Денег не хватит для покупки предмета n")
#         else:
#             self.__user_money = temp
#
# trade1 = Trade(5000)
# print(trade1.user_money)
#
# item_cost = random.randint(10,10000)
# print("Стоимость предмета", item_cost)
# trade1.user_money = item_cost
#
# print(trade1.user_money)




# class Temperature:
#     def __init__(self, celsius = 0):
#         self.__celsius = celsius
#
#     @property
#     def celsius(self):
#         return self.__celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         self.__celsius = value
#
#     @property
#     def fahrenheit(self):
#         return (self.__celsius * 9/5) + 32
#
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.__celsius = (value - 32) * 5/9
#
#
# temp = Temperature()
#
# print(temp.celsius)
# print(temp.fahrenheit)
#
# temp.celsius = 15
# print(f"Температура {temp.celsius} градусов цельсия = {temp.fahrenheit} градусов фаренгейта")
#
# temp.fahrenheit = 451
# print(f"Температура {temp.fahrenheit} градусов фаренгейта = {temp.celsius} градусов цельсия")







# class Car:
#     def __init__(self, name, speed):
#         self.__name = name
#         self.__speed = speed
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @property
#     def speed(self):
#         return self.__speed
#
#     @speed.setter
#     def speed(self, new_speed_value):
#         self.__speed = new_speed_value
#
#     def print_info_car(self):
#         print(f"Название машины: {self.__name} и скорость: {self.__speed}")
#
# car1 = Car("Niva", 50)
# print(car1.name)
# car1.print_info_car()
#
#
# class Truck(Car):
#
#     def carry_load(self):
#         print("The truck is carrying cargo")
#
# truck1 = Truck("Iveco", 100)
# truck1.print_info_car()
# truck1.carry_load()







# Сделайте два класса: главный класс - это класс Человек с атрибутами имя, возраст,
# а также с геттером и сеттером (для имени и возраста) и выводом информации о человеке.

# Второй класс "Водитель" унаследован от класса Человек
# и имеет две функции - водить легковую машину и водить грузовую машину.

































































