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
PREFERENCE_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/preference_list.txt'

people = []
drinks = []
preference = {}

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

def clear_screen():
    os.system("clear")

def print_main_menu():
    clear_screen()
    print(Menu)

#Input helper funcs

def get_menu_input(message):
    try:
        return int(input(f"{message} "))
    except ValueError:
        output("Menu items - numbers are the only input I understand")
        wait()
        return False

def user_input(selection_message):
    return input(f"{selection_message} \n") # return function for the def to return the input

def wait():
    input("Press enter to continue \n")

def input_people(input_message):
    return input(f"{selection_message} \n")

#Output helper funcs

def output (text):
    print(f"\n{text}")


def print_menu(title, data):
    items = []
    for i, item in enumerate(data, start=0): #list number for preference 5
        items.append(f"[{i}] {item}")
    clear_screen()
    print(f"{title}\n")
    print('\n'.join(items), '\n')

def print_preferences(data):
    items = []
    for name, drink in data.items():
        items.append(f"{name}: {drink}")
    print_table('Preference', items)


## Input helper funcs
def validate_menu_input(index, data):
    if index < 0 or index >= len(data):
        print(f'"{index}" is not a valid option from that menu\n')
        wait()
        return False
    return True

def select_from_menu(message, data):
    print_menu(message, data)
    index = get_menu_input('Enter your selection:')
    if not validate_menu_input(index, data):
        return False
    return data[index]

def load_list_from_file(path):
    data = []
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                if line == "":
                    continue
                data.append(line.strip())
        return data
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

#Data persistence helper funcs

def load_preferences(people,drinks):
    item = []
    for item in load_list_from_file(PREFERENCE_FILE_PATH):
        person,drink = item.split(":", 1)
        if person in people and drink in drinks:
            preference[person] = drink
        else:
            print("Unexpected data returned when loading favourites.")
            print(f"Drink is known: {drink in drinks}")
            print(f"Name is known: {name in people}")

    
def load_data():    
    for person in load_list_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_list_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)
    load_preferences(people,drinks)

def save_data(path, data):
    try:
        with open(path, 'w') as file:
            file.writelines([f'{item}\n' for item in data])
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')


def save_preferences(path,data):
    items = []
    for item in data.items():
        name, drink = item
        items.append(f'{name}:{drink}')
        save_data(PREFERENCE_FILE_PATH, items) 


def run():
    while True:
        print_main_menu()
        user_selection = user_input("Enter your selection or press enter to exit:\n")   # the def function input answers are stored in user_selection variable
        if user_selection == "":
            save_data(PEOPLE_FILE_PATH, people)
            save_data(DRINKS_FILE_PATH, drinks)
            save_data(PREFERENCE_FILE_PATH, preference)
            save_preferences(PREFERENCE_FILE_PATH, preference)
            exit()

        elif user_selection == "[1]" or user_selection == "1":
            print_table('PEOPLE', people)
            wait()  

        elif user_selection == "[2]" or user_selection == "2":
            print_table('DRINKS', drinks)
            wait()

        elif user_selection == "[3]" or user_selection == "3":
            input_name = user_input("Enter a name: \n")
            if input_name == "":
                print("No name entered")
                wait()
            else:
                input_name_title = input_name.title()
                if input_name_title not in people:
                    people.append(input_name_title)
                    print(f"{input_name_title} has been added to the list.")
                    print_table("PEOPLE", people)
                    save_data(PEOPLE_FILE_PATH, people)      
                    wait()
    
        # elif user_selection == "[3]" or user_selection == "3":
        #     while True:
        #         input_name = user_input("Enter a name: \n")
        #         if input_name == "":
        #             print("No name entered")
        #             yesorno = user_input("Do you want to try again?\nYes or No\n")
        #             if yesorno.title() == "No" or yesorno.title() == "N":
        #                 save_data(PEOPLE_FILE_PATH, people)
        #                 exit()
                            
        #             elif yesorno.title() == "Yes" or yesorno.title() == "Y":
        #                 input_name = user_input("Enter a name: \n")
        #                 input_name_title = input_name.title()
        #                 if input_name not in people:
        #                     people.append(input_name_title)
        #                     print(f"{input_name_title} has been added to the list.")
        #                 print_table("PEOPLE", people)
        #                 save_data(PEOPLE_FILE_PATH, people)
                    
        #         else:
        #             input_name_title = input_name.title()
        #             if input_name not in people:
        #                 people.append(input_name_title)
        #                 print(f"{input_name_title} has been added to the list.")
        #             print_table("PEOPLE", people)
        #             save_data(PEOPLE_FILE_PATH, people)      
        #             wait() 

        elif user_selection == "[4]" or user_selection == "4":
            input_drink = user_input("Enter a drink: \n")
            if input_drink == "":
                print("No name entered")
                wait()
            else:
                input_drink_title = input_drink.title()
                if input_drink not in people:
                    drinks.append(input_drink_title)
                    print(f"{input_drink_title} has been added.")
                    print_table("DRINKS", drinks)
                    COUNT_DOWN = 3  
                    wait()

        elif user_selection == "[5]" or user_selection == "5":
            person = select_from_menu('Choose a person', people)
            if not person:
                output(f'{person} is not in the list')
                wait()
            drink = select_from_menu(f'Choose a drink for {person}', drinks)
            if not drink:
                wait()
            preference[person] = drink
            print(f"\nThank you - {person}'s favourite drink is now {drink}")
            wait()

        elif user_selection == "[6]" or user_selection == "6":
            print_preferences(preference)
            save_preferences(PREFERENCE_FILE_PATH, preference)
            wait()
    
        elif user_selection == "[7]" or user_selection == "7":
            print('Saving data...')
            save_data(PEOPLE_FILE_PATH, people)
            save_data(DRINKS_FILE_PATH, drinks)
            save_data(PREFERENCE_FILE_PATH, preference)
            save_preferences(PREFERENCE_FILE_PATH, preference)

            print(f"Thank you for using {APP_NAME}")
            exit()

        else:
            print(f"I don't recognise that. Please try again later.")
    print(f"Thank you for using {APP_NAME}")

def start():
    load_data()
    run()
start()