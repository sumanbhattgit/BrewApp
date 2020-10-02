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
    input("Press enter to continue \n")0

def input_people(input_message):
    return input(f"{selection_message} \n")
