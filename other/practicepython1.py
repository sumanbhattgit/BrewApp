#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

# def exercise_1():
#     name = input("what's your name?\n")

# age = int(input("what's your age?\n"))
# year = 2020 + (100 - age)

# print(f"Your name is {name.title()} and you're {str(age)} years old. You will turn 100 years old in {year}.")
# #print(f"Your name is {name.title()} and you're" + str(age) + f" years old. You will turn 100 years old in {year}.")

# number = int(input("Enter a number:\n"))
# print("----")
# for i in range(number):
#     print(number)

#Exercise 3:
# Asking for input
def get_number():
    user_input = int(input("Enter a number:\n"))
    print("______")
    return user_input

def get_i():
# write a program that prints out all the elements of the list that are less than 5.
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
    b = []
    #get user input
    number = get_number()

    for i in a:
        if i < number:
            b.append(i)
            print(i)
    print(b)  
    print("Printed") 
# get_i()

#Extra:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# user_input = int(input("Enter a number: \n"))
# for i in a:
#     if i < user_input:
#         b.append(i) 
#         print(i)
# print(b)
# print("Printed!")

##Exercise 4
##Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# num = int(input("Please choose a number to divide: \n"))

# listRange = list(range(1,num+1))

# divisorList = []

# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)

#Exercise 5
#Returns a list that contains only the elements that are common between the lists (without duplicates)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []

# for i in a: 
#     if i in b:
#         if i not in c:
#             c.append(i)
# print(c)

#Exercise 6:
#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)
