import time
import random
import os
import shutil

# first_name = "uygar"
# last_name = "muntas"
# full_name = first_name + last_name
# print(first_name)
# print("name")
# print("hello" + " " + full_name)
# print(type(first_name))
# age = 20
# age = age + 1 # age+=1
# print(age)
# print(type(age))
# print("your age is = " + str(age))
# height = 186.7
# print(height)
# print(type(height))
# print("your height is = " + str(height)+"cm")
# human = True
# print(human)
# print(type(human))
# print(type(str(age)))
# print("are you a human =" + str(human))
##################################################
# first , second , third = "uygav" , 21 , True
# import math

# print(first)
# print(second)
# print(third)
##################################################
# first = second = third = fourth = 50
# print(first)
# print(second)
# print(third)
# print(fourth)
##################################################
# name = "uygar muntas"
# print(len(name))
# print(name.find("y"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("u"))
# print(name.replace("r","v"))
# print(name*2)
##################################################
# x = 1 # int
# y = 2.0 # float
# z = "3" # str

# x = float(x)
# y = int(y)
# z = int(z)

# print(x)
# print(y)
# print(z*3)
# print("x is = " + str(x))
##################################################
# name = input("what is your name :")
# age = int(input("what's your age :"))
# height = float(input("how tall are you?:"))
# age = age + 1
# print("hello"+ " " +name)
# print("you are " + str(age) + " years old ")
# print("you are " + str(height) + "cm tall")
##################################################
# pi = 3.14
# x=1
# y=2
# z=3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))
##################################################
# indexing[start:stop:step]
# name = "uygar muntas"
# first_name = name[0:3]
# last_name = name[4:]
# funky_name = name[0:8:3]
# reversed_name = name[::-1]
# zort_name = name[::2]
# print(zort_name)
##################################################
# slide(start,stop,step)
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])
##################################################
# age = int(input("how old are you?:"))
#
# if age>=18:
#     print("you are an adult")
# elif age < 0:
#     print("you haven't been born yet")
# elif age == 100:
#     print("you are a century old")
# else:
#     print("you are a child")
##################################################
# temp = int(input("what is the temperature outside?:"))
#
# if temp >= 0 and temp <=30:
#     print("the temperature is good today!")
#     print("go outside !")
# elif temp < 0 or temp > 30:
#     print("the temperature is bad today!")
#     print("stay inside!")
##############################
# temp = int(input("what is the temperature today?:"))
# if not(temp<0 or temp >30):
#     print("the temperature is good today!")
#     print("you can go outside")
# elif not(temp >=0 and temp <=30):
#     print("the temperature is bad today")
#     print("you shouldn't go outside")
##################################################
# name = ""
# while len(name) ==0
#     name = input("enter your name")
# print("hello" + name)
##################################################
# for i in range(10):
#     print(i)
#####################
# for i in range(50,100):
#     print(i)
#####################
# for i in range(50,100,2):
#     print(i)
#####################
# for i in "uygar":
#     print(i)
#####################
# for i in range(10):
#     print("hello")
##################################################
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("happy new year ! :)")
##################################################
# rows = int(input("how many rows ? :"))
# columns = int(input("how many columns ? :"))
# symbol = input("enter a symbol to use ?")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print()
##################################################
# while True:
#     name = input("enter your name:")
#     if name !="":
#         break
#####################
# phone_number = "123-456-789"
# for i in phone_number:
#     if i =="-":
#         continue
#     print(i,end="")
#####################
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)
##################################################
# food = ["pizza","hamburger","pasta","spaghetti","pudding"]
# food[0] = "sushi"
# print(food[0])
# food.append("ice cream")
# food.remove("pasta")
# food.insert(0,"cake")
# food.sort()
# food.pop()
# food.clear()
# for x in food:
#     print(x)
##################################################
# drinks = ["coffe","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake","ice cream"]
# food = [drinks,dinner,dessert]
# print(food[1][2])
##################################################
# student = ("uygar",20,"male")
# print(student.count("uygar"))
# print(student.index("male"))
# for x in student:
#     print(x)
# if "uygar" in stuent:
#     print("uygar is here !")
##################################################
# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup"}
# dinner_table = utensils.union(dishes)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

# for x in dinner_table:
#     print(x)
#####################
# utensils ={"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
##################################################
# capitals = {'Turkey':'Ankara',
#             'Macedonia':'Skopje',
#             'China':'Beijing',
#             'India':'New Dehli'}
# print(capitals['Macedonia'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# capitals.update({'Germany','Berlin'})
# capitals.update({'Turkey','Luleburgaz'})
# capitals.pop('India')
# capitals.clear()
# for key,value in capitals.items():
#     print(key,value)
##################################################
# name = "bro Code!"
# if(name[0].islower()):
#     name = name.capitalize()
# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)
##################################################
# def hellofunc(name):
#     print("hello " + name)
#     print("have a nice day!")
# my_name = "uygar"
# hellofunc(my_name)
#####################
# def hello(first_name,last_name,age):
#     print("hello"+first_name+" "+last_name)
#     print("you are "+str(age)+" years old")
#     print("have a nice day!")
# hello("uygar","muntas",20)
##################################################
# def multiply(number1,number2):
#     result = number1*number2
#     return result
# x = multiply(6,8)
# print(x)
#####################
# def multiply(number1,number2):
#     return number1 * number2
# x = multiply(6,8)
# print(x)
##################################################
# def hello(first,middle,last):
#     print("hello"+first+" "+middle+" "+ last)
# hello(last="zort",middle="muntas",first="uygar")
##################################################
# num = input("enter a whole positive number")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
####################
# print(round(abs(input("enter a whole positive number"))))
##################################################
# name = "uygar"     #global scope
# def display_name():
#     name = "code"
#     print(name)
# display_name()
# print(name)
####################
# name = "uygar"
# def display_name():
#     print(name)
# display_name()
##################################################
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3,4,5,6))
####################
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
##################################################
# def hello(**kwargs):
#     print("hello "+kwargs['first']+"",kwargs['last'])
# hello(first="uygar",middle="muntas",last="zort")
##############################
# def hello(**name):
#     print("hello",end=" ")
#     for key,value in name.items():
#         print(value,end=" ")
# hello(title="mr.",first="bro",middle="dude",last="code")
##################################################
# animal = "cow"
# item = "moon"
# print("the " + animal + " jumped over the "+item)
# print("the {} jumped over the {}".format(animal,item))
# print("the {1} jumped over the {0}".format(animal,item))
# print("the {1} jumped over the {1}".format(animal,item))
##############################
# print("the {item} jumped over the {animal}".format(animal="cow",item="moon"))
# print("the {animal} jumped over the {animal}".format(animal="cow",item="moon"))
##############################
# animal ="cow"
# item ="moon"
# text = "the {} jumped over the {}"
# print(text.format(animal,item))
##################################################
# name = "bro"
# print("hello my name is {}".format(name))
# print("hello my name is {:10}.Nice to meet you".format(name))
# print("hello my name is {:<10}.Nice to meet you".format(name))
# print("hello my name is {:>10}.Nice to meet you".format(name))
# print("hello my name is {:^10}.Nice to meet you".format(name))
##################################################
# pi_number= 3.14159
# number = 1000
# print("the number pi is{:.3f}".format(pi_number))
# print("the number is {:,}".format(number))
# print("the number is {:b}".format(number))
# print("the number is {:o}".format(number))
# print("the number is {:X}".format(number))
# print("the number is {:E}".format(number))
##################################################
# x = random.randint(1,6)
# y = random.random()
# print(x)
# print(y)
##############################
# my_list = ['rock','paper','scissors']
# z = random.choice(my_list)
# print(z)
##############################
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print(cards)
##################################################
# try:
#     numerator = int(input("enter a number to divide :"))
#     denominator = int(input("enter a number to divide by :"))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("you can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("something went wrong! :(")
##################################################
# try:
#     numerator = int(input("enter a number to divide :"))
#     denominator = int(input("enter a number to divide by :"))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("you can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("something went wrong! :(")
# else:
#     print(result)
# finally:
#     print("this will always execute")
##################################################
# path = "C:\\Users\\UYGAV\\OneDrive\\Masaüstü\\testpython.txt"
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("that location doesn't exist !")
##################################################
# with open('text.txt') as file:
#     print(file.read())
# print(file.closed)
##############################
# try:
#     with open('text.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file wasn't found :(")
##################################################
# text = "overwatchsombratr1\nThis is some text\nHave a good one!\n"
# with open('text.txt','w') as file:
#     file.write(text)
##############################
# text = "have a nice day !"
# with open('text.txt','a') as file:
#     file.write(text)
##################################################
# shutil.copyfile('text.txt','copy.txt') #src,dst
##############################
# shutil.copy('text.txt','copy.txt')
##############################
# shutil.copy2('text.txt','copy.txt')
##################################################
# source = "move.text"
# destination = "C:\\Users\\UYGAV\\OneDrive\\Masaüstü\\testpython.txt"
#
# try:
#     if os.path.exists(destination)
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was not found")
# except FileNotFoundError:
#     print(source+" was not found")
##################################################
# path = "delete.txt"
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not have permission to delete that")
##############################
# path ="empty_folder"
# try:
#     os.rmdir(path)
# except FileNotFoundError:
#     print("that file was not fount")
# except PermissionError:
#     print("you do not have permission to delete that")
# except OSError:
#     print("you cannot delete that using that function")
# else:
#     print(path+" was deleted")
##################################################
# path="empty_folder"
# try:
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not have permission to delete that")
# except OSError:
#     print("you cannot delete that using that function")
# else:
#     print(path+" was deleted")


#os.remove(path)   delete a file
#os.rmdir(path)    delete an empty directory
#shutil.rmtree(path) delete a directory containing files

##############################
# import messages
# messages.hello()
# messages.bye()
##############################
# import messages as msg
# msg.hello()
# msg.bye()
##############################
# from messages import hello,bye
# hello()
# bye()
##############################
# from messages import *
# hello()
# bye()
##############################
# pre-writen modules
# help("modules")
################################################## Object Oriented Programming and class variable
# from car import Car
# car_1 = Car("chevy","corvette",2021,"blue")
# car_2 = Car("ford","mustang",2022,"red")
#
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# car_1.drive()
# car_1.stop()
# car_2.drive()
# car_2.stop()
# print(car_1.wheels)
# car_2.wheels = 2
# print(car_2.wheels)
# print(Car.wheels)
##############################
# from car import Car
#
# car_1 = Car("chevy","corvette",2021,"blue")
# car_2 = Car("ford","mustang",2022,"red")
#
# Car.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)
################################################## inheritance
# class Animal:
#     alive = True
#
#     def eat(self):
#         print("this animal is eating")
#     def sleep(self):
#         print("this animal is sleeping")
#
# class Rabbit(Animal):
#     def run(self):
#         print("this rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("this fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("this hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()
################################################## multi-level inheritance
# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print("this animal is eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("this dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()
################################################## multiple inheritence
# class Prey:
#     def flee(self):
#         print("this animal flees")
#
# class Predator:
#     def hunt(self):
#         print("this animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey,Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
##################################################
# class Car:
#      def turn_on(self):
#         print("you start the engine")
#         return self
#
#      def drive(self):
#          print("you drive the car")
#          return self
#      def brake(self):
#          print("you step on the brakes")
#          return self
#
#      def turn_off(self):
#          print("you turn off the engine")
#          return self
#
# car = Car()
# car.turn_on().drive()
# car.brake().turn_off()
#
# car.turn_on()
# car.drive()
# car.brake()
# car.turn_off()
#
# car.turn_on().drive().brake().turn_off()
#
# car.turn_on()\
#      .drive()\
#      .brake()\
#      .turn_off()
################################################# super function
# super() = function used to give access to the methods of a parent class.
# returns a temporary object of a paren class when used
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
# class Square(Rectangle):
#     def __init__(self,length,width):
#         super().__init__(length,width)
#     def area(self):
#         return self.length*self.width
# class Cube(Rectangle):
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3,3)
# cube = Cube(3,3,3)
#
# print(square.area())
# print(cube.volume())

################################################# abstract classes
# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

# from abc import ABC,abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print("you drive a car")
#     def stop(self):
#         print("this car is stopped")
# class Motorcycle(Vehicle):
#     def go(self):
#         print("you ride the motorcycle")
#     def stop(self):
#         print("this motorcycle is stopped")
#
# vehicle = Vehicle() # we cant use
# car = Car()
# motorcycle = Motorcycle()

# vehicle.go() # we cant use
# car.go()
# motorcycle.go()
# motorcycle.stop()

################################################# objects as arguments
# class Car:
#     color = None
# class Motorcycle:
#     color = None
#
# def change_color(vehicle,color):
#     vehicle.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
# change_color(car_1,"red")
# change_color(car_2,"white")
# change_color(car_3,"blue")
# change_color(bike_1,"black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

################################################# duck typing
# class Duck:
#     def walk(self):
#         print("this duck is walking")
#     def talk(self):
#         print("this duck is qwuacking")
#
# class Chicken:
#     def walk(self):
#         print("this chicken is walking")
#     def talk(self):
#         print("this chicken is clucking")
#
# class Person():
#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print("you caught the critter!")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(duck)
# person.catch(chicken)

################################################# walrus operator :=
# print(happy:=True)
##############################
# foods = list()
# while True:
#     food = input("what food do you like ? :")
#     if food == "quit":
#         break
#     foods.append(food)

########## same with walrus operator
# foods = list()
# while food := input("what food do you like") != "quit":
#     foods.append(food)

################################################## functions to variables
# def hello():
#     print("hello")
#
# print(hello())
#
# hello()
# print(hello)
# hi = hello
# print(hi)
# hi()
#########
# say = print
# say = ("wow :O")

################################################## higher order functions

# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(func):
#     text = func("hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

####################

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))

################################################## lambda usage

# def double(x):
#     return x*2
# print(double(5))

##############################

# double = lambda x : x*2
# print(double(5))
# multiply = lambda x, y: x*y
# print(multiply(5,6))
# add = lambda x, y, z: x+y+z
# print(add(5,6,7))
# full_name = lambda first_name , last_name : first_name+" "+ last_name
# print(full_name("uygar","muntas"))
# age_check = lambda age:True if age>=18 else False
# print(age_check(18))

################################################## sort

# students = ["squidward","sandy","patrick","spongebob","mr.krabs"]
# students.sort(reverse=True)
#
# for i in students:
#     print(i)
####################
# students = ("squidward","sandy","patrick","spongebob","mr.krabs")
# students.sort()
# print(students)
####################
# students = ("squidward","sandy","patrick","spongebob","mr.krabs")
# sorted_students = sorted(students,reverse=True)
#
# for i in sorted_students:
#     print(i)

##############################
# students = [("squidward","F",60),
#             ("sandy","A",33),
#             ("patrick","D",36),
#             ("spongebob","B",20),
#             ("mr.krabs","C",78)]
#
# age = lambda ages:ages[2]
# students.sort(key=age,reverse=True)
#
# for i in students:
#     print(i)
##############################

# students = [("squidward","F",60),
#              ("sandy","A",33),
#              ("patrick","D",36),
#              ("spongebob","B",20),
#              ("mr.krabs","C",78)]
# age = lambda ages:ages[2]
# sorted_students = sorted(students,key=age)
#
# for i in sorted_students:
#     print(i)

################################################## map
# map(func,iterable)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
#
# to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)
#
# store_euros = list(map(to_euros,store))
# store_dollars = list(map(to_dollars,store))
#
# for i in store_euros:
#     print(i)
# for j in store_dollars:
#     print(j)

############################## same example without lambda

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
#
# def to_euros (data):
#     return (data[0], data[1]*0.82)
#
# store_euros = list(map(to_euros,store))

################################################## filter
# filter(function,iterable)


# friends = [("rachel",19),
#            ("monica",18),
#            ("phoebe",17),
#            ("joey",16),
#            ("chandler",21),
#            ("ross",20)]
#
# age = lambda data:data[1] >=18
#
# drinking_buddies = list(filter(age,friends))
#
# print(drinking_buddies)
#
# for i in drinking_buddies:
#     print(i)

################################################## reduce
# reduce(function,iterable)

# import functools
#
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x ,y:x+y,letters)
#
# print(word)

#################### different ex

# import functools
#
# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x,y:x*y,factorial)
# print(result)

################################################## list comprehension

# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

#################### same things with single line

# squares = [i*i for i in range(1,11)]
# print(squares)

#################### different example

# students = [100,90,80,70,60,50,40,30,0]
# passed_students = list(filter(lambda x:x>=60,students))
# print(passed_students)

#################### same result other way
# students = [100,90,80,70,60,50,40,30,0]
# passed_students = [i for i in students if i >=60]
#
# print(passed_students)

#################### different example

# students = [100,90,80,70,60,50,40,30,0]
# passed_students = [i if i >= 60 else "FAILED" for i in students]
# print(passed_students)

################################################## dictionary comprehension
# dictionary = {key: expression for (key,value) in iterable}


# cities_in_F = {'New York': 32,'Boston': 75,'Los Angeles': 100,'Chicago' :50}

# cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

# print(cities_in_C)

############################## different example
# dictionary = {key : expression for (key,value) in if conditional}

# weather = {'New York':"snowing",'Boston':"sunny",'Los Angeles':"sunny",'Chicago':"cloudy"}
# sunny_weather = {key : value for (key,value) in weather.items() if value =="sunny"}
# print(sunny_weather)

############################## different example
# dictionary = {key : (if/else) for (key,value) in iterable}

# cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# desc_cities = {key:("WARM" if value>=40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

############################## different example

# dictionary = {key : function(value) for (key,value) in iterable}

# def check_temp(value):
#     if value >= 70:
#         return "HOT"
#     elif 69 >= value >= 40:
#         return "WARM"
#     else:
#         return "COLD"
#
# cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# desc_cities = {key : check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

################################################## zip func

# usernames = ["dude","bro","mister"]
# passwords = ["p@ssword","abc123","guest"]
# users = zip(usernames,passwords)
# print(type(users))
# for i in users:
#     print(i)

####################
# usernames = ["dude","bro","mister"]
# passwords = ["p@ssword","abc123","guest"]
# users = dict(zip(usernames,passwords))
# print(type(users))
# for key,value in users.items():
#     print(key+ " : "+value)

##############################

# usernames = ["dude","bro","mister"]
# passwords = ["p@ssword","abc123","guest"]
# login_date = ["1/1/2021","1/2/2021","1/3/2021"]
# users = zip(usernames,passwords,login_date)
# for i in users:
#     print(i)

################################################## if__name__ == '__main__'



# print(__name__)
#
# if __name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")

################################################## time module

import time

# print(time.ctime(0))
# print(time.ctime(100000))

####################

# print(time.time())
# print(time.ctime(1682548878.28668))
# print(time.ctime(time.time()))

####################

# time_object = time.localtime()
# print(time_object)

####################

# https://docs.python.org/3/library/time.html

# local_time = time.strftime("%B %d %Y %H %M %S",time_object)
# print(local_time)

####################

# time_object2 = time.gmtime()
# print(time_object2)

####################

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

####################

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

####################

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

################################################## threading

# import threading
# import time
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())
# def eat_breakfast():
#     time.sleep(3)
#     print("you eat breakfast")
# def drink_coffee():
#     time.sleep(4)
#     print("you drank coffee")
# def study():
#     time.sleep(5)
#     print("you finish studying")

# eat_breakfast()
# drink_coffee()
# study()

##############################

# x = threading.Thread(target=eat_breakfast,args=())
# x.start()
#
# y = threading.Thread(target=drink_coffee,args=())
# y.start()
#
# z = threading.Thread(target=study,args=())
# z.start()
#
# x.join()
# y.join()
# z.join()


################################################## daemon threading

# import threading
# import time
#
#
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for : ",count," seconds")
#
# x = threading.Thread(target=timer,daemon=True)
# x.start()
# answer = input("do you wish to exit ?")

################################################## multi-processing
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)

# from multiprocessing import Process,cpu_count
# import time
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
# def main():
#     a = Process(target=counter,args=(100000,))
#     b = Process(target=counter,args=(100000,))
#     c = Process(target=counter, args=(100000,))
#     d = Process(target=counter, args=(100000,))
#
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#
#
#
#     print("finished in:",time.perf_counter(),"seconds")
#
#
# if __name__ == '__main__':
#     main()

################################################## gui windows
# from tkinter import *
#
# # widgets = gui elements : buttons , txt boxes , labels , images,
# # windows = serves as a container to hold or contain these widgets
#
# window = Tk() #instantiate an instance of a window
# window.geometry("420x420")
# window.title("uygarrrr")
#
# # icon = PhotoImage(file='shikamaru.jpg')
# # window.iconphoto(True,icon)
#
# # window.config(background='orange')
# window.config(background="#14e8ff")
#
# window.mainloop() #place window on computer screen

################################################## label

# from tkinter import *
#
# window = Tk()
#
# # photo = PhotoImage(file='C:\\Users\\UYGAV\\OneDrive\\Masaüstü\\fotolarim\\friends1.jpg')
# # i couldn't do this photo , i'll try later
#
# label = Label(window,
#               text="hello world",
#               font=('Arial',40,'bold'),
#               fg='red',
#               bg='yellow',
#               relief=SUNKEN,
#               bd=10,
#               padx=20,
#               pady=20,
#               compound='top')
#
# label.pack()
# # label.place(x=15,y=0)
#
#
# window.mainloop()

################################################## button

# from tkinter import *
#
#
# count = 0
# def click():
#     global count
#     count +=1
#     print(count)
#
# window = Tk()
#
# button = Button(window,
#                 text="click me !",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="red",   # foreground
#                 bg="yellow",    # background
#                 activebackground="black",
#                 activeforeground="green",
#                 state=ACTIVE)  #default
# # you can add image
# button.pack()
#
# window.mainloop()

################################################## entry box

# from tkinter import *
#
# def submit():
#     username = entry.get()
#     print("hello "+username)
#     entry.config(state=DISABLED)
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1,END)
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial",50),
#               fg="green",
#               bg="black",
#               show="*")
# # entry.insert(0,'insert ')
# entry.pack(side=LEFT)
#
# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=LEFT)
#
# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=LEFT)
#
# window.mainloop()

################################################## checkbox

# from tkinter import *
#
# def dispalay():
#     if(x.get()==1):
#         print("you agree!")
#     else:
#         print("you dont agree")
#
# window = Tk()
#
# x = IntVar() # you can use stringVar or booleanVar
#
# check_button = Checkbutton(window,
#                            text="i agree to something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=dispalay,
#                            font=('Arial',20),
#                            fg='green',
#                            bg='black',
#                            activeforeground='green',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            )
# # you can also add image
#
# check_button.pack()
#
# window.mainloop()

################################################## radio button

# from tkinter import *
#
# food =["pizza","hamburger","hotdog"]
#
# def order():
#     if(x.get()==0):
#         print("you ordered pizza!")
#     elif(x.get()==1):
#         print("you ordered a hamburger!")
#     elif(x.get()==2):
#         print("you ordered a hotdog!")
#     else:
#         print("huh?")
#
# window = Tk()
#
# x = IntVar()
#
# for index in range(len(food)):
#     radio_button = Radiobutton(window,
#                                text=food[index], # adds text to radio buttons
#                                variable=x, # groups radiobuttons together if they share the same variable
#                                value=index,  # assigns each radiobutton a different value
#                                padx=25, # adds padding on x-axis
#                                font=("Impact",50),
#                                indicatoron=0, # eliminate circle indicators
#                                width=25, # sets width of radio button
#                                command=order, # set command of radiobutton to function
#                                )
#     radio_button.pack(anchor=W)
#
# window.mainloop()


################################################## scale
# from tkinter import *
#
# def submit():
#     print("the temperature is : " + str(scale.get()) + " degrees C")
#
# window = Tk()
# # you can also add images
# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL, # orientation of scale
#               font=('Consolas',20),
#               tickinterval=10, # adds numeric indicators for value
#               showvalue=1, #hide current value
#               resolution=5, # increment of slider
#               troughcolor="yellow",
#               fg='red',
#               bg='#69EAFF'
#               )
# scale.set((scale['from']+scale['to'])/2) # set current value of slider
#
# scale.pack()
#
# button = Button(window,
#                 text='submit',
#                 command=submit,
#                 )
# button.pack()
#
#
# window.mainloop()


################################################## listbox
from tkinter import *

############# def submit():
#############     print(listbox.get(listbox.curselection())) you can use this func but you'll get a error about multiple option

# def submit():
#     food=[]
#
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#     for index in food:
#         print(index)
#
# def add():
#     listbox.insert(listbox.size(),entry_box.get())
#     listbox.config(height=listbox.size())
#
# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#     listbox.config(height=listbox.size())
#
# window = Tk()
#
# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",20),
#                   width=15,
#                   selectmode=MULTIPLE)
# listbox.pack()
# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")
#
# listbox.config(height=listbox.size())
#
# entry_box = Entry(window)
# entry_box.pack()
#
# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack()
#
# add_button = Button(window,text="add",command=add)
# add_button.pack()
#
# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack()
#
# window.mainloop()

################################################## messagebox

# from tkinter import *
# from tkinter import messagebox  # import messagebox library
#
#
#
# def click():
#     messagebox.showinfo(title='info message box',
#                         message='are you sure')
#
# def click2():
#     while(True):
#         messagebox.showwarning(title='WARNING!',message='are you sure')
#
# def click3():
#     messagebox.showerror(title='error',message='something went wrong')
#
# def click4():
#     if messagebox.askokcancel(title='ask ok cancel',message='message '):
#         print('you did a thing')
#     else:
#         print('you canceled a thing')
#
# def click5():
#     if messagebox.askretrycancel(title='ask ok cancel',message='message '):
#         print('you did a thing')
#     else:
#         print('you canceled a thing')
#
# def click6():
#     if messagebox.askyesno(title='ask yes or no',message='are you sure'):
#         print('you said yes')
#     else:
#         print('you said no')
#
# def click7():
#     answer = messagebox.askquestion(title='ask question',message='do you like pie?')
#     if(answer=='yes'):
#         print('i like pie too :)')
#     else:
#         print('why do you not like pie? :(')
#
# def click8():
#     answer = messagebox.askyesnocancel(title='you no cancel',message='do you like to code?',icon='warning')
#     if(answer==True):
#         print("you like to code")
#     elif(answer==False):
#         print("then why are you here?")
#     else:
#         print("you have dodged the question")
#
# window = Tk()
#
# button = Button(window,
#                 text='click me',
#                 command=click8)
# button.pack()
#
#
#
# window.mainloop()


################################################## color chooser

# from tkinter import *
# from tkinter import colorchooser  # submodule
#
# def click():
#     color = colorchooser.askcolor()
#     print(color)
#     colorHex = color[1]
#     print(colorHex)
#     window.config(bg=colorHex)
#
# def click2():
#     color = colorchooser.askcolor()
#     window.config(bg=color[1]) # change background color
#
# def click3():
#     window.config(bg=colorchooser.askcolor()[1])
#
# window = Tk()
#
# window.geometry("420x420")
# button = Button(text='click me',command=click2)
# button.pack()
#
# window.mainloop()

################################################## text area

# from tkinter import *
#
# def submit():
#     input = text.get("1.0",END)
#     print(input)
# window = Tk()
#
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20)
# text.pack()
#
# button = Button(window,text="submit",command=submit)
# button.pack()
#
# window.mainloop()


################################################## file dialog

# from tkinter import *
# from tkinter import filedialog
#
# def openFile():
#     filepath = filedialog.askopenfilename()
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()
#
# window = Tk()
# button=Button(text="Open File",command=openFile)
# button.pack()
# window.mainloop()

################################################## save a file

# from tkinter import *
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\UYGAV\\PycharmProjects\\pythonTutorial",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file",".html"),
#                                         ("All files",".*"),
#                                     ])
#     filetext = str(text.get(1.0,END))
#     file.write(filetext)
#     file.close()
#
# window = Tk()
#
# button = Button(text='save',command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
#
# window.mainloop()

################################################## menubar

# from tkinter import *
#
# def openFile():
#     print("File has been opened")
#
# def saveFile():
#     print("File has ben saved")
#
# def cut():
#     print("you cut some text")
#
# def copy():
#     print("you copied some text")
#
# def paste():
#     print("you pasted some text")
#
# window = Tk()
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile)
# fileMenu.add_command(label="Save",command=saveFile)
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit)
#
# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)
# ### you can also add some images
#
# window.mainloop()


################################################## frames

# from tkinter import *
#
# window =Tk()
#
# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.place(x=0,y=0)
#
# Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)
#
# window.mainloop()


################################################## new window

# from tkinter import *
#
# def create_window():
#     new_window = Tk()
#
#     main_window.destroy()
#
# main_window = Tk()
#
# Button(main_window,text="create new window",command=create_window).pack()
#
# main_window.mainloop()

################################################## windows tabs
# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
#
# notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook) # new frame for tab 1
# tab2 = Frame(notebook) # new frame for tab 2
#
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both") # expand = expand to fill any space not otherwise used
#                                         # fill = fill space on x and y axis
# Label(tab1,text="Hello , this is tab 1")
# Label(tab2,text="goodbye , this is tab 2")
#
# window.mainloop()

################################################## grid
# from tkinter import *
#
# # grid () = geometry manager that organizes widgets in a table-like structure in a parents
#
# window = Tk()
#
# titleLable = Label(window,text="Enter you info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)
#
# firstNameLabel = Label(window,text="First Name:",width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)
#
# lastNameLabel = Label(window,text="Last Name :",bg="green").grid(row=2,column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)
#
# emailLabel = Label(window,text="email:",bg="blue",width=30).grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=2,column=1)
#
# submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
#
# window.mainloop()


################################################## progress bar

# from tkinter import *
# from tkinter.ttk import *
# import time
#
# def start():
#     GB = 10
#     download = 0
#     speed = 1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()
#
# button = Button(window,text="download",command=start).pack()
#
# window.mainloop()


################################################## canvas

# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill="purple",width=2)
# canvas.create_line(0,500,500,0,fill="green",width=2)
# canvas.create_rectangle(50,50,150,150,fill="red")
# point = [350,0,250,250,0,250]
# canvas.create_polygon(point,fill="yellow",outline="black",width=5)
# canvas.create_arc(0,0,350,350,style=PIESLICE,start=180,extend=180)
# canvas.pack()
#
#
# window.mainloop()

################################################## keyboard events

# from tkinter import *
#
# def doSomething(event):
#     print("you pressed: " + event.keysym)
#     label.config(text=event.keysym)
#
#
# window = Tk()
#
# window.bind("<Key>",doSomething)
#
# label = Label(window,font=("Helvetica",50))
# label.pack()
#
# window.mainloop()


################################################## mouse events

from tkinter import *

def doSomething(event):
    print("mouse coordinates:" + str(event.x) + ","+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) # left mouse click
window.bind("<Button-2>",doSomething) # scroll wheel
window.bind("<Button-3>",doSomething) # right mouse click
window.bind("<ButtonRelease>",doSomething)
window.bind("<Enter>",doSomething) # enter the window
window.bind("<Leave>",doSomething) # leave the window
# #### window.bind("<Motion>",doSomething) # where the mouse moved

window.mainloop()







