import pymysql

# def read_order_info_database():
#     connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
#     cursor = connection.cursor()
#     cursor.execute('SELECT ID, Owner from Order_info')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     cursor.close()
#     connection.close()

# def read_order_items_database():
#     connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
#     cursor = connection.cursor()
#     cursor.execute('SELECT Order_ID, PersonID, Drink from Order_items')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     cursor.close()
#     connection.close()

def read_round_database():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    cursor.execute('SELECT OrderID, First_Name, Last_Name, Drink_Name from Round')
    rows = cursor.fetchall()
    people_list = []

    for row in rows:
        first_name = row[1]
        last_name = row[2]
        fullname = " ".join((first_name, last_name))
        people_list.append(fullname) 
    return people_list
    cursor.close()
    connection.close()


def uploading_round_to_the_database(OrderID, Round_Owner, First_Name, Last_Name, Drink_Name):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    mysql = "INSERT INTO Round (OrderID, Round_Owner, First_Name, Last_Name, Drink_Name) VALUES ({}, '{}', '{}', , '{}', '{}')". format(OrderID, Round_Owner, First_Name, Last_Name, Drink_Name)
    cursor.execute(mysql)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    read_round_database()
    uploading_round_to_the_database()
    # read_order_info_database()
    # read_order_items_database()
    # preference_dict = read_preference_database()
    # print(preference_dict)


