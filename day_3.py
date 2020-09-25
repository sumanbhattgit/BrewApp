#TASK:
# Use the input built-in function to build a CLI menulike this (or better)
#Welcome to BrIW v0.1!
#Please, select an option by entering a number:
# [1] Get all people
# [2] Get all drinks
# [3] ExitEnter your selection:

#assinging values to our variables
GET_PEOPLE = 1
GET_DRINKS = 2
EXIT = 3
APP_NAME ="BrIW v0.1"

#Doc string used to print the menu
Menu = f"""
Welcome to {APP_NAME}!
Please, select an option by entering a number: 
[1] Get all people 
[2] Get all drinks 
[3] Exit
"""
#define names
people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]

#Check arguments-Except only one command at a time

#Table output helper funcs
# Define function to call up parameter later on in the script
def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f"| {item}")
    print_separator(width)


def print_header(title, width):
    print_separator(width) 
    print(f"| {title}")
    print_separator(width)
    
def selection_screen ():
    print(MENU)

def user_input():
    return int(input())


while True:
    print(Menu)
    user_selection = int(input("Enter your selection: \n"))
    print(user_selection)

if user_input == "GET_PEOPLE":
    for name in people:
        print(name)

        #if they want to continue 
        #don't : print
    print("Thank you for your input.")
elif user_input == [2] or user_input == 2:
    for drink in drinks:
        print(drink)
    print("Thank you for your input.")
else:
    print("I don't recognise that, please choose 1 or 2")
user_continue = 'y'
while user_continue == 'y':
    user_input = int(input("Please, select an option by entering a number: \n[1] Get all people \n[2] Get all drinks \n"))
    if user_input == [1] or user_input == 1:
        for name in people:.
            print(name)
        user_continue = input("Do you want to continue? \n")
        if they want to continue 
        don't : print
        print("Thank you for your input.")
    elif user_input == [2] or user_input == 2:
        for drink in drinks:
            print(drink)
        user_continue = input("Do you want to continue? \n")
        print("Thank you for your input.").