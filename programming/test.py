# mylist = ["banana", "cherry", "apple", "pineapple", "orange"]
# item = mylist[1]
# print(item)
# print(mylist)
# for i in mylist:
#     print(i)

# if "banana" in mylist:
#     print("yes")
# else: 
#     print("no")

# if "lemon" in mylist:
#     print("yes")
# else:
#     print("no")

# if "orange" and "pineapple" in mylist:
#     print("yes")
# else:
#     print("no")
# result = len(mylist)
# print(result)
# mylist.append("lemon")
# print(mylist)

# mylist.insert(1, "Nigeria")
# print(mylist)
# print(mylist)
# item = mylist.pop()
# print(mylist)
# item = mylist.remove("banana")
# print(mylist)
# # item1 = mylist.reverse()
# # print(item1)
# item1 = mylist.reverse()
# print(mylist)

# print(mylist)
# item = mylist.reverse()
# # print(item)
# print(mylist)

# mylist = [1, 2, 4, 6, -8, -1, -2]
# mylist.sort()
# print(mylist)
# item = mylist.sort()
# # print(item)
# print(mylist)
# print(mylist)
# new_list = sorted(mylist)
# print(mylist)
# print(new_list)
# mylist = [0] * 5
# print(mylist)

# mylist = [3] * 9
# print(mylist)
# mylist = [2] * 5
# print(mylist)

# mylist2 = [2, 4, 3, 7, 1, 8, 9]

# result = mylist + mylist2
# print(result)

# mylist = [1, 2, 3, 4, 7, 4, 8, 9, 1]
# a = mylist[1:5]
# a = mylist[:5]
# a = mylist[1:]
# b = mylist[1::]
# a = mylist[::-1]
# b = mylist[::-2]
# c = mylist[::-3]
# print(a)
# print(b)
# print(c)

# list_org = ["banana", "cherry", "apple"]
# print(list_org)
# list_crg = list_org[:]
# print(list_crg)
# # item = list_crg.reverse()
# # print(list_crg)
# # print(list_crg.reverse())
# list_crg.append("lemon")
# # print(list_crg)
# print(list_org)
# mylist = [1, 3, 2, 4, 5, 2, 4, 7, 9]
# b = [i*i for i in mylist]

# print(mylist)
# print(b)

# Tuple 16: 38
# mytuple = ("max",)
# # print(mytuple)
# print(type(mytuple))
# mytuple = tuple(["max", 28, "Boston"])
# print(mytuple)

# item = mytuple[-1]
# print(item)

# try:
#     print(x)
# except:
#     print("An error just occured")

# try:
#     print(x)
# except NameError:
#     print("Variable is not defined")
# except:
#     print("something else went wrong")

# try:
#     print(x)
# except:
#     print("Somthing went wrong")
# finally:
#     print("the 'try except' is finished ")

# username = input("Enter username: ")
# print("Your name is  " + username)

# casting is specifying the data type of a variable
# x = str(3)
# y = int(3)
# z = float(3)
# print(x, y, z)
# # There is a type function
# print(type(x))
# print(type(y))
# print(type(z))

# python variable names are case sensitive and declared using the
# snake-case
# x, y, z = "orange", "mango", "Apple"
# print(x, y, z)

# x = y = z = "orange"
# print(x)
# print(y)
# print(z)
# unpacking is extracting values in a list, tuple into variables
# fruits = ["apple","orange","apple"]
# x, y, z = fruits
# # print(x, y, z)
# print(x)
# print(y)
# print(z)
# python uses + operator to combine both text and varaible
# global variable can be used both inside and outside of a function 
# name = "awesome"

# def myfunc():
#      print("Python is " + name)

# myfunc()

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()
# print("Python is " + x)
# variable  can store different data type and different data type can do different things
# you can convert from data type to another using int(), str(), float() method
# python does not have a random function but has an inbuilt module for it

# import random

# print(random.randrange(1, 10))
# python is an object oriented language and as such it uses classes to define it data type
# x = """ 
#     python is an object oriented language and as such it uses classes to define it data type
#    python is an object oriented language and as such it uses classes to define it data type
#    """
# print(x)
# x = "Hello World"
# print(x[0])
# print(x[1])
# print(x[2])
# strings are array
# you can loop through string
# x = "Hello World"
# for i in x:
#     print(i) 
# we can also have string length 
# x = "Hello, free World"
# # print(len(x))
# if "expensive" not in x:
#     print("yes expensive is not present")
# slicing of string

# x = "Hello world"
# print(x[2:5])
# x = "Hello world"
# print(x[:5])
# x = "Hello World"
# print(x[0:])
# string has some inbuilt methods
# upper case
# x = "Hello World"
# print(x.upper())
# x = 'Hello World'
# print(x.lower())
# string strip method
# x = "  Hello, World"
# # print(x)
# print(x.strip())
# x = "Hello World"
# print(x.replace("H","F"))
# a = "Hello,  world"
# x = a.split(',')
# print(x)
# print(type(x))
# # print(a.split(","))

# x = 37
# txt = "Hello world"
# result = x + txt
# print(result)

# x = "Hello "
# y = "World"
# z = x + y
# print(z)
# age = 36
# txt = "My name is John, and  I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.9
# myorder = "I want {} pieces of item {} for {} dollars. "
# print(myorder.format(quantity, itemno, price))
# txt = "This is a new level \"in this program\" \n for decagon student"
# print(txt)
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)
# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
# if b > a:
#     print(True)
# else:
#     print(False)
# print(bool("Hello"))
# print(bool(15))
# x = 15
# print(isinstance(x, int))
# x = 15
# y = 9.1
 
# if x > y:
#     print(isinstance(y, int))
# else:
#     print(isinstance(y, float))
# isinstance is used to check if an object is of certain data type
# mylist = ['apple', 'banana', "pineapple"]
# list is created using a square bracket
# print(mylist)
# list items are ordered, changeable, and allow duplicate values
# mylist = ["apple","banana","apple","orange"]
# print(len(mylist))
# print(type(mylist))
# there is a list constructor
# this_list = list(("apple","orange","pineapple","yam","melon","kiwi","mango","cherry","tomatoes"))
# print(this_list)
# print(this_list[0])
# print(this_list[-1])
# print(this_list[2:5])
# print(this_list[:4])
# if "cola" in this_list:
#     print('yes, apple is present in the list')
# else:
#     print("This fruit is not present in the list")

# name = input("enter your name: ")

# if name == "zanders":
#     # print(True)
#     pass

# if 1 == 1:
#     print("True")
# x = int(True)
# y = int(False)
# print(x, y)
# z = 1 > 0
# if z:
#     print(True)
# x = 100
# if x == 1 or x == 100:
#     print("True")
# x = 100
# y = "zander"

# pseudo code 
# An input to accept user age value
# To know whether the value entered is greater than 18
# if value is greater than 18, the user is allowed to take course
# if value entered is less than, then user are told they can't 
# Then user are told how many years is left to take course

# age_checker = int(input("Enter your age: "))
# requiredAge = 18

 
# if age_checker >= 60:
#     print("You are eligible for discount on our course")
# elif age_checker == 30:
#     print("you are eligible for half price")
# elif age_checker >= 18 and age_checker < 60:
#     print("You are welcome to our course")

#     if age_checker == 20:
#         print("you are eligible for a special offer")
        
# else: 
#     print("you are not permitted to take this until you are 18 years old")
#     years_to_go = 18 - age_checker
#     print(f"You have {years_to_go} year's left to take the course")

# x = 2
# y = 1

# if x > y: print("x is greater than y")

# x = 2
# y = 4

# print("x") if x > y else print("y")

# pseudo code
#  Create an application which will check the users password they enter to the password
# held in a variable. write an output for both a failed and successful match

# Enter_password = input("Enter your password: ")
# password = "mypass@"

# if Enter_password == password:
#     print("Your password is a correct match")
# else:
#     print("your password was not a correct match")
#     Enter_password = input("Enter your password: ")

# Extending the password matching features, only users who correctly enter the password and called
# by the name of zander should have access to the secret code! Extend the application to allow 
# users to input their name as well as the password. if usernames and passwords match correctly
# print out - you have access, if not, let the user know they can not enter.
    

# Enter_name = input("Enter your name: ")
# Enter_password = input("Enter your password: ")
# password = "mypass@"
# expected_name_match = "zander"

# if Enter_password == password and Enter_name == expected_name_match:
#     print("You have access")

# else:
#     # Enter_password = input("Pls, enter your passowrd again: ")
#     print("your password was not a correct match")

# x = range(3)
# # my_list = []
# for i in x:
#     print(i)

# x = range(3, 6)
# for n in x:
#     print(n)

# pseudo code
# A user input to enter coins
# To determine user level

# number_of_coins = int(input("Enter the amount of coins that you have: "))

# if number_of_coins > 0 and number_of_coins <= 20:
#     print("Bronze level ")
# elif number_of_coins >= 21 and number_of_coins <= 40:
#     print("Silver level")
# elif number_of_coins >= 41:
#     print("Gold level")
# else:
#     print("sorry enter a correct value")

# numerator = 10
# denominator = 0
# print(numerator / denominator)

# try: 
#     # code that may cause exception
# except:
#     #  code to run when exception occurs

# try: 
#     # code that may cause exception
# except:
#     #  code to run when exception occurs

# try:
#     numerator = int(input("Enter memo"))
#     denomiantor = int(input("Enter demo"))
#     result = numerator / denomiantor
#     print(result)
# except:
#     print("Denomiantor cannot be 0. Please try again")

# double = lambda n: n*n
# print(double(3))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# square = lambda n: n*n
# squared_nums = []
# for n in numbers:
#     squared_nums.append(square(n))

# print(squared_nums)

# A map() takes two arguments a function and an iterator
# numbers = [1, 2, 3, 4, 5]
# square_nums = list(map(lambda n: n*n, numbers))
# print(square_nums)  