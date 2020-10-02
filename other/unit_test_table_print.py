def clear_screen():
    os.system("cls")

def print_menu(title, data):
    items = []
    for counter, item in enumerate(data, 1): #list number for preference 5
        items.append(f"[{counter}] {item}")
    clear_screen()
    print(f"{title}\n")
    print('\n'.join(items), '\n')



def test_print_menu():
#We use patch when stubbing or spying
#Often used for python standard libraries or built-in
    system = "os.system"
#assert
#make title
    title = "Suman"
    data
    system.assert_called_once_with("cls")
    print("Printing")

def test_print_menu():
#Arrange
#Act
#Assert 
