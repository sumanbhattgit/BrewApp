#Dictionaries keys has to be unique. Key:Value

import os

GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
Input_People_ARG = 3
Input_Drinks_ARG = 4
Set_Your_Preference_ARG = 5
Preference_Printout_ARG = 6
EXIT_ARG = 7

APP_NAME ="BrIW" 
VERSION  = "0.1"
COUNT_DOWN = 3

Menu = f"""
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number: 
[1] Get all people 
[2] Get all drinks 
[3] Input People
[4] Input Drinks
[5] Set_Your_Preference
[6] Preference_Printout
[7] Exit
"""
PEOPLE_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/people_list.txt'
DRINKS_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/drink_list.txt'

people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]
preference = {}

#Table to look nice and all

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
    print(Menu)

def user_input(selection_message):
    return input(f"{selection_message} \n") # return function for the def to return the input

def wait():
    input("Press enter to return to the menu \n")

def input_people(input_message):
    return input(f"{selection_message} \n")

# def clear_screen():
#     os.system("clear")

# def print_main_menu():
#     clear_screen()
#     print(MENU_TEXT)

#Loading the data


# def load_list_from_file(path):
#     data = []
#     try:
#         with open(path, 'r') as file:
#             for line in file.readlines():
#                 data.append(line.strip())
#             return data
#     except FileNotFoundError:
#         print(f'No file can be found at path: "{path}"')
#         exit()
#     except Exception as e:
#         print(f'Unable to load data from "{path}" with error: {str(e)}')


# def save_data():
#     with open(PEOPLE_FILE_PATH, 'w') as file:
#         file.writelines([f'{person}\n' for person in people])
#     with open(DRINKS_FILE_PATH, 'w') as file:
#         file.writelines([f'{drink}\n' for drink in drinks])


# def load_data():
#     for person in load_list_from_file(PEOPLE_FILE_PATH):
#         people.append(person)
#     for drink in load_list_from_file(DRINKS_FILE_PATH):
#         drinks.append(drink)

def run():
    while True:
        print_menu()
        user_selection = user_input("Enter your selection or press enter to exit:\n")   # the def function input answers are stored in user_selection variable
        if user_selection == "":
            print("You pressed enter")

        elif user_selection == "[1]" or user_selection == "1":
            print_table("PEOPLE", people)
            Count_down = 3
            wait()
    

        elif user_selection == "[2]" or user_selection == "2":
            print_table("DRINKS", drinks)
            Count_down = 3
            wait()
   
    
        elif user_selection == "[3]" or user_selection == "3":
            input_name = user_input("Enter a name: \n")
            input_name_title = input_name.title()
            if name not in people:
                people.append(input_name_title)
                print(f"{input_name_title} has been added.")
            print_table("PEOPLE", people)
            Count_down = 3 
            wait() 

        elif user_selection == "[4]" or user_selection == "4":
            input_drink = user_input("Enter a drink: \n")
            input_drink_title = input_drink.title()
        if name not in people:
            people.append(input_drink_title)
            print(f"{input_drink_title} has been added.")
            print_table("DRINKS", drinks)
            Count_down = 3  
            wait()

        elif user_selection == "[5]" or user_selection == "5":
            name_preference = user_input("What's your name: \n")
            drink_preference = user_input("What's your favourite drink: \n")
            print(f"You're {name_preference.title()} and your favourite drink is set to {drink_preference}. \n")
            preference[name_preference.title()] = [drink_preference.title()]
            print(preference)
            wait()

        elif user_selection == "[6]" or user_selection == "6":
            get_preference = user_input("Input a name to find their favourite drink\n")
            drink_printout = preference.get(get_preference.title())
            print(drink_printout)
            wait()
    

        elif user_selection == "[7]" or user_selection == "7":
            print('Saving data...')
            save_data()
            print(f'Thank you for using {APP_NAME}')
            exit()

        else:
            Count_down -= 1
            print(f"I don't recognise that, you have {Count_down} tries left. Otherwise, the programme will quit.")
            if Count_down == 0:
                break 
    print("Thank you for your input.")

def start():
    run()

start()