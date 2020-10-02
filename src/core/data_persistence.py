import csv
from constant import PEOPLE_FILE_PATH, DRINKS_FILE_PATH, PREFERENCE_FILE_PATH

people = []
drinks = []
preference = {}

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
                data.append(line[0])
        print(data)
        return data
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

def load_preferences(people,drinks):
    try:
        items = load_list_from_file(PREFERENCE_FILE_PATH)
        print(items)
        for item in items:
            print(item)
            person,drink = item.split(":", 1) #### fix this
            if person in people and drink in drinks:
                preference[person] = drink
            else:
                print("Unexpected data returned when loading favourites.")
                print(f"Drink is known: {drink in drinks}")
                print(f"Name is known: {name in people}")
    except ValueError:
        print(f"Unable to load preference list with error")
        
def load_data():    
    for person in load_list_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_list_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)
    load_preferences(people,drinks)
    return

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
        name, drink = item
        items.append(f'{name}:{drink}')
        save_data(PREFERENCE_FILE_PATH, items) 