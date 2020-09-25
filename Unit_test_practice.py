
def remove_list_element(my_list, element):
    """Removes specified element from specified list,
IF the element is a string that contains only characters, and can not be
empty, have all the characters be spaces, contain any numbers or be already not in the list. """
    if not element or element.isspace():
        print("You have not entered anything!")
    elif any(num in element for num in "0123456789"):
        print("No numbers can be included in the name.")
    elif element.capitalize() in my_list:
        my_list.remove(element.capitalize())
        print(f"Your choice: {element.capitalize()} was successfully removed!")
    else:
        print(f"{element.capiltalize()} is not in the list already.")
    return my_list


def test_remove_list_element():
    #Arrange
    my_list = ["Suman" , "Katy", "Chloe"]
    element = "Chloe"

    expected_output = ["Suman", "Katy"]

    #Act
    actual_output = remove_list_element(my_list, element)

    #Assert
    assert actual_output == expected_output
    print("SUCCESSFUL!")

test_remove_list_element()