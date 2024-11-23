# import section
import math
import os
import numpy as np
from datetime import datetime

print("PART 1: Python Basics \n \n")
print("Lesson 1: Introduction to Python \n")
print("exo  1 : Write a program that prints your name. \n")
print("hi i am ayoub bezai")


print("Lesson 2: Variables and Data Types\n")
print("exo  1 : Write a program that stores your age and converts it to a string.. \n")

age = 15
age  = str(age)
print(type(age))


print("Lesson 3: Input and Output Operations \n")
print("exo  1 :Write a program that asks for your favorite color and prints a message using that color \n")
favColor = input("enter ur favorite color:  ")
print(f"ur favorite color is:{favColor} ")


print("Lesson 4: Control Structures (if-else and Loops) \n")
print("exo  1 :Write a program that prints all even numbers from 1 to 10. \n")

print("method one")
for i in range(2,11,2):
    print(i)

print("method two")
j=2
while j <= 10:
     print(j)
     j=j+2

print("method three")
def even(k):
    print(k)
    if k%2 == 0:
        return print("done")
    else:
        return even(k+2)

even(2)

print("method four")
for i in range(1,11):
    if i % 2 == 0:
        print(i)



print("Lesson 5: Lists, Tuples, and Dictionaries \n")
print("exo  1 :Create a list of three student names and print the second name. \n")
studentsNames = ["ayoub","ahmed","mohamed"]
print("the name of the secend student is : ",studentsNames[1])



print("Lesson 6: Functions and Modules \n")
print("exo  1 :Create a function that adds two numbers and returns the result.\n" )
def addTwoNumbers(number1,number2) :
    return number1+number2
print("enter two numbers \n")

numberOne = int(input("enter first number: \n "))
numberTwo = int(input("enter second number: \n "))
print("the result is : " ,addTwoNumbers(numberOne ,numberTwo))




print("Lesson 7: File Management Basics \n")
print("exo  1 :Write a program that creates a folder named 'test_dir' in the current directory.\n" )
print("the OS package has been imported \n")
print("the current directory is : ",os.getcwd(),"\n")

if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
    print("the directory 'test_dir'  has been created \n")
else:
    print("the 'test_dir' directory already exists \n")



print("Lesson 8: Error Handling with try-except \n")
print("exo  1 :Write a program that attempts to open a non-existent file and prints a custom error message.\n" )
try :
    with open("noneExistent.txt","r") as file :
        print(file.read())
except FileNotFoundError:
    print("the file 'noneExistent.txt' does not exist \n")



print("Lesson 9: Python Packages (Installing and Importing) \n")
print("exo  1 :Install the requests package and write a program to print the current date and time using it.\n" )
print("we imported 'import numpy as np ' in the start\n" )
print("and installed the package by writing in the terminal #'pip install numpy'\n" )
print("and installed the request  package by writing in the terminal #'pip install requests '\n" )
print("we imported 'from datetime import dateTime' in the start\n" )
print(datetime.today(),"\n")




print("Lesson 10: Practice Quiz on Python Basics \n")
print("exo  1 :questions.\n" )
print("1 :What is the difference between a list and a tuple?.\n" )
print("2. Write a function that multiplies two numbers and returns the product.\n" )
def mulTwoNumbers(number1,number2) :
    return number1*number2
print("enter two numbers \n")

numberOne = int(input("enter first number: \n "))
numberTwo = int(input("enter second number: \n "))
print("the result is : " ,mulTwoNumbers(numberOne ,numberTwo))
print("\n" )
print("3. What will be the output of the following code? \n" )
# for i in range(1, 4):
#  print(i * "*")
print("i t will be : \n"
      "*\n"
      "**\n"
      "***\n"
      )