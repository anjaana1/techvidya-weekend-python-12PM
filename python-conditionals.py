# Conditionals in Python
# if,elif,else
# >,>=,<,<=,==,!=   -> Comparision Operators


# If Condition
# Syntax:
# if (condition == True):
#     block of if condition

# age = 28
# if age > 18:
#     print("You are eligible to vote")
# print("if condition ended")


# if-else condition
# Syntax:
# if (condition == True):
#     block of if
# else:
#     block of else

# age = int(input("Enter your age :"))
# if age > 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible")

# num1 = 30
# num2 = 20
# if num1 > num2:
#     print(str(num1) + " is greater than " + str(num2))
# else:
#     print(str(num1) + " is less than " + str(num2))


# if-elif-else
# syntax :
# if (condition == True):
#     block of if
# elif (condition == True):
#     block of this elif
# elif (condition == True)
#     block of this elif
# else:
#     block of else

# age = int(input("Enter your age : "))

# age < 18 and age > 0     OR    0 < age < 18
#
# if age == 18:
#     print("You are eligible to vote from this year")
# elif age > 18:
#     print("You are perfectly eligible to vote")
# elif 0 < age < 18:
#     print("Sorry, You are not eligible")
# else:
#     print("Wrong Input")


# Nested if
# if cond:
#     block of codes
#     if cond:
#         block of codes
#     else:
#         block of codes
# else:
#     block of codes


# x = 5
# if x > 10:
#     print("Greater than 10,")
#     if x > 20:
#         print("also greater than 20")
#     else:
#         print("less than 20")
# else:
#     pass


# Pass Keyword
# if codn:
#     pass


# # Short Hand If - Else
# x = 11
# if x > 10:
#     print("Greater than 10")
# else:
#     print("Smaller than 10")
#
# print("Greater than 10") if x > 10 else print("Smaller than 10")


# age = int(input("Enter your age : "))

# if age == 18:
#     print("You are eligible to vote from this year")
# elif age > 18:
#     print("You are perfectly eligible to vote")
# elif 0 < age < 18:
#     print("Sorry, You are not eligible")
# else:
#     print("Wrong Input")

# print("You are eligible to vote from this year") if age == 18 else print("You are perfectly eligible to vote") \
    # if age > 18 else print("Sorry, You are not eligible") if 0 < age < 18 else print("Wrong Input")


# Assignment
# Write a program to print whether a number is positive, negative or zero of a user input.(Long and short-hand)
# Write a python program to convert temperature from celcius to fahrenheit, and fahrenheit to celcius.
# (c/5=f-32/9)
# Write a program to guess a number between 1 to 10.



# Using If-Else with And/Or
# a = 200
# b = 33
# c = 500
# if a > b and a > c:
#     print("a is greater than b and c")
# elif b > a and b > c:
#     print("b is greater than a and c")
# elif c > a and c > b:
#     print("c is greater than a and b")
# else:
#     print("Wrong Input")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#     print("At least one condition is True")