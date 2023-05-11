# name = "This is a string"
# print("Hello " + name)

# print(type(name))

# first_name = "John"
# last_name = "Pratt"
# full_name = first_name + " " + last_name
# print(full_name)

# age = 21
# age += 1
# print(type(age))
# print("Your age is: " + str(age))

# height = 250.5
# print(height)
# print(type(height))
# print("Your height is: " + str(height) + "cm")

# human = False
# print(human)
# print(type(human))
# print("Are you Human: " + str(human))

# name = "John"
# age = 21
# attractive = True
# print(name)
# print(age)
# print(attractive)

#Multiple Assignment
# name, age, attractive = "John", 21, True
# print(name, age, attractive)

#String Methods
# name = "John Pratt"
# print(len(name))
# print(name.find("P"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.count("a"))
# print(name.replace("John", "Little John"))
# print(name * 3)


#typecasting =  converting one datatype to another
# x = 1
# y = 2.0
# z = "3"
# y = int(y)
# z = int(z)
# print(z*3)

#name = input("What is your name? ")
# print("Hello " + name + "!")

# age = int(input("What is your age? "))
# age = age + 1
# print("Your age is: " + str(age))

# height = float(input("What is your height? "))
# print("You are ", str(height), "cm tall")

# import math

# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(-4))
# print(pow(2,4))
# print(math.sqrt(49))
# x = 1
# y = 2
# z = 3
# print(max(x,y,z))
# print(min(x,y,z))

# string slicing - create a substring by extracting elements from another string

# indexing[]
# slice()
# [start:stop:step]

# name = "John Pratt"
# first_name = name[0:4]
# print(first_name)
# last_name = name[5:10]
# last_name = name[5:]
# print(last_name)
# funky_name = name[0:10:3]
# print(funky_name)
# reversed_name = name[::-1]
# print(reversed_name)

# website = "http://www.google.com"
# slice = slice(11,-4)
# website[slice]
# print(website[slice])

#prints apple instead of whole site by string slicing
# website_1 = "https://www.apple.com"
# slice = slice(12,-4)
# print(website_1[slice])

# if statements = block of code

# age = int(input("How old are you?"))
# if age >= 18 and age < 65:
#     print("You are an adult!")
# elif == 100:
#     print("You are a Century!")
# elif age < 0:
#     print("You haven't been born yet")
# elif age >= 65 and age <= 99:
#     print("You are a senior citizen")
# else:
#     print("You are a child")

#Logical Operators (and, or, not)

# temp = int(input("What is the temperature outside?"))
# if not(temp >= 0 and temp <= 30):
#     print("The temp is bad today")
#     print("Stay inside")
# elif not(temp < 0 or temp > 30):
#     print("You are between 0 and 30")
#     print("Go outside")

#while loops -statement that executes block of code as long as condition remains true
# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name)

#for loops - a statement that wil execute its block of code a limited anuon of times
# while loop = unlimited
# for loop = limited

# for i in range(10):
#     print(i+1)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "John Pratt":
#     print(i)

# import time 

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Happy New Year")

#nested loops - have one loop inside of another loop.  Inner loop will finish all iterations
#               before finishing one iteration of outer loop

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

#Loop Control statements - Change a loops execution from its normal sequence.

#break - used to terminate loop entirely
#continue - skips to the next iteration of the loop
#pass - does nothing, acts as a placeholder

# while True: 
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "618-514-7605"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
    
#     if i == 13:
#         pass
#     else:
#         print(i)

# list - used to store multiple items in a single variable

# food = ["pizza", "hamburgers", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi"

# food.append["ice cream"] # adds value to end
# food.remove("hotdog") # removes hotdogs
# food.pop() #removes last item
# food.instert(0, "cake") #adds cake at index 0
# food.sort() #sorts list alphabetically
# food.clear() #removes all elements oflist

# # print(food[0]) #will print sushi

# for x in food:
#     print(x)

#2D Lists in python - A lists of lists(Multi Dimentional Lists)

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks,dinner,dessert]

# print(food[2][1])

#Tuple = collection which is ordered and unchangeable
#        used to group together related data

student = ("bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")















