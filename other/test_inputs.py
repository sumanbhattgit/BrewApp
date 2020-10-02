import unittest
from unittest.mock import Mock, patch
# from Week2_loadfile_csv_loadclass import select_option_from_menu
from other.appv2 import select_option_from_menu, user_input



# def select_option_from_menu(message, data):
#     print_menu(message, data)
#     counter_num = get_menu_input('Enter your selection:')
#     if not validate_menu_input(counter_num, data):
#         return False
#     return data[counter_num - 1]

class Test_Select_Option_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    @patch("Week2_loadfile_csv_loadclass.print_menu")
    @patch("Week2_loadfile_csv_loadclass.get_menu_input")
    @patch("Week2_loadfile_csv_loadclass.validate_menu_input")
    def test_when_number_is_returned_from_select_option_from_menu(self,mock_validate_menu_input,mock_get_menu_input, mock_print_menu):
        # Arrange
        # Make msg
        message = "suman"
        # make data
        data = ["Sue", "S"]
        #Patch  print menu
        #patch  get menu input
        mock_get_menu_input.return_value = 2
        #patch validate menu input
        mock_validate_menu_input.return_value = True
        expected = "S"
        # Act
        actual = select_option_from_menu(message,data)
        # Assert
        self.assertEqual(actual, expected)
        mock_print_menu.assert_called_once_with("suman", ["Sue", "S"])


    # @patch("Week2_loadfile_csv_loadclass.print_menu")
    # @patch("Week2_loadfile_csv_loadclass.get_menu_input")
    # @patch("Week2_loadfile_csv_loadclass.validate_menu_input")
    # def test_when_number_is_not_returned_from_select_option_from_menu(self,mock_validate_menu_input,mock_get_menu_input, mock_print_menu):
    #     #ARRANGE
    #     message = "suman"
    #     data = ["Sue", "S"]
    #     mock_get_menu_input.return_value = 2
    #     mock_validate_menu_input.return_value = False

    #     #ACT
    #     actual = 

    #     self.assertFalse(actual)
    #     self.assertEqual(actual, None)


# def print_main_menu():
#     clear_screen()
#     print(Menu)

#     Arrange


# def test_print_main_menu(unittest.TestCase):

# def user_input(selection_message):
#     return input(f"{selection_message} \n")

class Test_User_Input(unittest.TestCase):
    def test_when_prints_something(self):
        # Arrange
        expected_output = "I'm struggling with unit testing!"
        #Act
        actual_input = user_input()
        #Assert
        assert actual_input == expected_output
        print("Great!")


# def print_menu(title, data):
#     items = []
#     for counter, item in enumerate(data, 1): #list number for preference 5
#         items.append(f"[{counter}] {item}")
#     clear_screen()
#     print(f"{title}\n")
#     print('\n'.join(items), '\n')

#ARRANGE
# title = 
#ACT
#ASSERT

# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()


