#TASK:
# Use the input built-in function to build a CLI menulike this (or better)
#Welcome to BrIW v0.1!
#Please, select an option by entering a number:
# [1] Get all people
# [2] Get all drinks
# [3] ExitEnter your selection:

#assinging values to our variables
#Good practice to assign all the global value at the start of the script
GET_PEOPLE = 1
GET_DRINKS = 2
EXIT = 3
APP_NAME ="BrIW v0.1"
Count_down = 3 # User has 3 tries to enter a correct option before the programme will quit

#Doc string used to print the menu
#f in the menu is like .format, APP_NAME is replaced it's value when the code is run)
menu = f"""
Welcome to {APP_NAME}!
Please, select an option by entering a number: 
[1] Get all people 
[2] Get all drinks 
[3] Exit
"""
#define names
people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]

#Check arguments - Except only one command at a time

#Table output
# Define function to call up parameter later on in the script
def print_table(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    width = get_table_width(title, data) # width of the table depends on the title and data
    print_header(title, width)  # print table which is defined in the (second) def function
    for item in data:   #for the print_table function the item (name or drink) in the data (people or drinks)
        print(f"| {item}" +  (" " *(width-len(item) - 2) + " |")) # this is purely for the formatting. width of the table - the length of a name/drink 
    print_separator(width)   #this is defined in another def function

def print_header(title, width): #this gets called by print_table()
    print_separator(width)  #==============================
    print(f"| {title}" +  (" " *(width-len(title) - 2) + " |")) # | "PEOPLE" or "DRINKS"  |
    print_separator(width)  #==========================
    
def print_separator(width): #this gets called by print_table() and print_header()
    print("=" * (width + 2)) # this is finding the longest width of our table + 2 to make a table

def get_table_width(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    longest = len(title)          # length of "PEOPLE"  "DRINKS"
    additional_spacing = 2         

    for item in data:           
        if len(item) > longest:     #checking for longest length of item (suman..//tea..) for our table
            longest = len(item)
    return longest + additional_spacing

def print_menu():
    print(menu)

def user_input(message):
    return input(f"{message} \n") # return function for the def to return the input

def wait():
    input("Press enter to return to the menu \n")

while True:
    print_menu()
    user_selection = user_input("Enter your selection:")   # the def function input answers are stored in user_selection variable
    if user_selection == "[1]" or user_selection == "1":
        print_table("PEOPLE", people)
        Count_down = 3

    elif user_selection == "[2]" or user_selection == "2":
        print_table("DRINKS", drinks)
        Count_down = 3
    
    elif user_selection == "[3]" or user_selection == "3":
        break

    else:
        Count_down -= 1
        print(f"I don't recognise that, you have {Count_down} tries left. Otherwise, the programme will quit.")
        if Count_down == 0:
            break 
print("Thank you for your input.")

