import csv
from src.core.table import print_table
from src.core.inputs import wait
import src.core.db2peoplelist as a
import src.core.db2drinklist as b
import src.core.db2preference as c
import src.core.db2round as d
from constant import PREFERENCE_FILE_PATH
from src.core.inputs import user_input
from src.core.menu import select_option_from_menu

preference_csv = {}

#Data persistence
def load_list_from_file(path):
    data = []
    try:
        with open(path, "r") as file:
            file_reader = csv.reader(file, delimiter = ",", quoting=csv.QUOTE_ALL)
            for line in file_reader:
                if not line and line == "":
                    continue
                if line == "\n":
                    continue
                data.append(line[0]) #removed a line after this
        return data
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

def load_preferences():
    try:
        items = load_list_from_file(PREFERENCE_FILE_PATH)
        for item in items:
            name_arr = item.split(":", 1)
            person = name_arr[0]
            drink = name_arr[1] #### Changed this
            preference_csv[person] = drink
        return preference_csv
    except ValueError:
        print(f"Unable to load preference list with error")


def save_data(path, data):
    try:
        with open(path, 'w', newline = "") as file:
            writer = csv.writer(file,delimiter = ",", quoting=csv.QUOTE_ALL)
            for element in data:
                writer.writerow([element])
    except FileNotFoundError as e:
        print(f'File "{path}" cannot be found')
    except Exception as e:
        print(f'Unable to open file "{path}". Error is "{e}".')

def save_preferences(path,data):
    items = []
    for item in data.items():
        people = a.read_people_database()
        drinks = b.read_drink_database()
        people, drinks = item
        items.append(f'{people}:{drinks}')
        save_data(PREFERENCE_FILE_PATH, items)

#output

def output (text):
    print(f"\n{text}")

def print_preferences(data):
    items = []
    for name, drink in data.items():
        items.append(f"{name}: {drink}")
    print_table('PREFERENCE', items)

#Menu inputs
def print_all_people():
    people = a.read_people_database()
    print_table('PEOPLE'.center(24), people)
    wait() 

def print_all_drinks():
    drinks = b.read_drink_database()
    print_table('DRINKS', drinks)
    wait()

def input_people_to_the_list():#############################OPTION 3
    input_name = user_input("Enter your first name: \n")
    if input_name == "":
        print("No name entered")
        return
    input_last_name = user_input("Enter your last name: \n")
    if input_last_name == "":
        print("No name entered")
        return
    input_age = user_input("Enter your age: \n")
    if input_age == "":
        print("I don't understand")
        return
    if input_age.isdigit():
        input_age_int = int(input_age)
    else:
        print("I don't understand")
        return
    
    input_name_title = input_name.title()
    input_last_name_title = input_last_name.title()
    print(f"{input_name_title}{input_last_name_title} has been added to the database.") 
    a.uploading_people_to_the_database(input_name_title, input_last_name_title, input_age)
    people = a.read_people_database()
    wait()
    

def input_drinks_to_the_list(): #############################OPTION 4
    input_drink = user_input("Enter a drink: \n")
    input_drink_title = input_drink.title()
    if input_drink == "":
        print("No name entered")
        wait()

    input_category = user_input("Enter a category: Coffee or Cocktails or Wine or Soft Drinks \n")
    input_category_title = input_category.title()
    if input_category == "":
        print("No name entered")
        wait()
    
    input_age_limit = user_input("Does it have alcohol: Yes or No \n")
    if input_age_limit == "":
        print("Enter Yes or No")
        wait()
        if input_age_limit.lower() in {"y","yes"}:
            age_limit_a = int(0)
        if input_age_limit.lower() in {"n","no"}:
            age_limit_a = int(1)    

    input_price = user_input("Enter price for the drink: \n")
    if input_price == "":
        print("No name entered")
        wait()
    if input_price.replace(".", "", 2).isdigit():
        input_price_float = float(input_price)
        
       
    print(f"{input_drink_title} has been added to the database.") 
    b.uploading_drink_to_the_database(input_drink_title, input_category_title, 1, input_price_float)
    drinks = b.read_drink_database()   
    wait()

def set_your_preference():
    people = a.read_people_database()       
    person = select_option_from_menu('Choose a person', people)
    name_arr = person.split(" ", 1)
    first = name_arr[0]
    last = name_arr[1]
    if not person:
        output(f'{person} is not in the list')
        wait()
    drinks = b.read_drink_database()    
    drink = select_option_from_menu(f'Choose a drink for {person}', drinks)
    if not drink:
        wait()
    preference = c.read_preference_database()    
    preference[person] = drink
    preference_csv[person] = drink
    save_preferences(PREFERENCE_FILE_PATH, preference_csv)
    print(f"\nThank you - {person}'s favourite drink is now {drink}")
    c.uploading_preference_to_the_database(first, last, drink, 1)
    wait()

def preference_printout():
    preference = c.read_preference_database() 
    print_preferences(preference)
    wait()

def exit_option():
    print('Saving data...')
    print(f"Thank you for using {APP_NAME}")
    exit()
