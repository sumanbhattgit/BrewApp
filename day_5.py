
import sys
args = sys.argv

people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]
preference = {}


def load_items(people_list):

    try: 
        with items_file =open("people_list.txt", "r")
        for line in items_file.readlines():
            people.append(line)
        items_file.close()
    except Exception as e:
        print( "An error occurred: " + str (e))
        return[]
    except:
        print(f"Unable to open {people_list} for writing")
        return[]

        for line in item_file.readlines():
            trimmed line = line[:-1]

    people_file = open("people.txt", "w")
    people_file.write("somehign to be added ") #overwrites
    people_file.close()







items_file = load_items("people_list.txt", people)
load_items("drink_list.txt", drinks)

def print_table(title, data): 
    width = get_table_width(title, data) 
    print_header(title, width)  
    for item in data:  
        print(f"| {item}" +  (" " *(width-len(item) - 2) + " |")) 
    print_separator(width)   

def print_header(title, width): #this gets called by print_table()
    print_separator(width)  #==============================
    print(f"| {title}" +  (" " *(width-len(title) - 2) + " |")) # | "PEOPLE" or "DRINKS"  |
    print_separator(width)  #==========================
    
def print_separator(width): 
    print("=" * (width + 2)) 

def get_table_width(title, data): 
    longest = len(title)          
    additional_spacing = 2         

    for item in data:           
        if len(item) > longest:     
            longest = len(item)
    return longest + additional_spacing

def print_menu():
    print(Menu)

def user_input(selection_message):
    return input(f"{selection_message} \n") 

def wait():
    input("Press enter to return to the menu \n")

def input_people(input_message):
    return input(f"{selection_message} \n")