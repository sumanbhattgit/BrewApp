       
# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"] 

# def suman(data):
#     items = []
#     for i, item in enumerate(data, start=0): #list number for preference 5
#         items.append(f"[{i}] {item}")
#     print(items)
#     return suman

# suman(people)
import csv

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
        return data
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

preference = load_list_from_file("C:/Users/suman/Desktop/BrewApp/preference_list.csv")
print(preference)

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

# people = load_list_from_file("C:/Users/suman/Desktop/BrewApp/p.csv")
# people.append("test")
# print(people)

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
# save_data("C:/Users/suman/Desktop/BrewApp/p.csv", people)

