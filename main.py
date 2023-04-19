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
#     def turn_on(self):
#         print("you start the engine")
#         return self
#
#     def drive(self):
#         print("you drive the car")
#         return self
#     def brake(self):
#         print("you step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("you turn off the engine")
#         return self
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
#     .drive()\
#     .brake()\
#     .turn_off()
##################################################
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())




