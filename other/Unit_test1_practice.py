def add_list_element(my_list, element):
    """Appends specified element to specified list,
IF the element is a string that contains only characters, and can not be
empty, have all the characters be spaces, contain any numbers or be already in the list. """
    for element in my_list:
        if not element or element.isspace():
            print("You have not entered anything!")
        elif any(num in element for num in "0123456789"):
            print("No numbers can be included in the name.")
        elif element.capitalize() not in my_list:
            my_list.append(element.capitalize())
            print(f"Your choice: {element.capitalize()} was successfully added!")
        else:
            print("Already on the list. Try a different option.")
    return my_list

#arrange
def test_add_list_element():
    element = "Sue"
    my_list = ["Sanj", "Katie", "Victor"]
    expected = my_list + [element]
#act
    actual = add_list_element(my_list, element)
#assert
    assert actual == expected
    print("SUCCESSFUL!")

test_add_list_element()

def add_people(new_name,people_list):
   # new_name = input("Please enter new name: ")
    people_list.append(new_name)
    return print(f'"{new_name}" has been added')

add_people("Saeed",people_list)
print(people_list)

def test_add_people():
    #Arrange
    apple =[]
    # people_list = ["Suman" , "Katy", "Claire"]
    new_name = "Chloe"
    expected = apple + ["Chloe"]
    # expected_output = ["Suman", "Katy", "Claire", "Chloe"]

    #Act
    actual_output = add_people(my_list, element)
    add_people(new_name,apple)

    #Assert
    assert actual_output == expected_output
    print("SUCCESSFUL!")

test_remove_list_element()

def get_table_width(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    longest = len(title)          # length of "PEOPLE"  "DRINKS"
    additional_spacing = 2         
    for item in data:           
        if len(item) > longest:     #checking for longest length of item (suman..//tea..) for our table
            longest = len(item)
        return longest + additional_spacing

def test_get_table_width():
    #ARRANGE
    title = "ANIMALS"
    data = ["Cow", "Goat", "Rhino", "Pig", "Hippopotamus"]
    expected = 14
    #ACT
    actual = get_table_width(title, data)
    #ASSERT
    assert actual == expected
    print("Get table function is on the right track!")

test_get_table_width()