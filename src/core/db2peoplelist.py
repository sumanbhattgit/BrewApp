import pymysql
from personclass import Person as Person

def read_people_database():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    
    # args = ("Hannah", "Mocha")
    cursor.execute('SELECT PersonID, First_Name, Last_Name from People') 
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


# if __name__ == "__main__":
    # read_people_database()

    # p_list = read_people_database()

    # print(p_list)


def uploading_people_to_the_database(First_Name, Last_Name, Age):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    mysql = "INSERT INTO People (First_Name, Last_Name, Age) VALUES ('{}', '{}', {})". format(First_Name, Last_Name, Age)
    cursor.execute(mysql)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    read_people_database()
    uploading_people_to_the_database()

    
    # p_list = uploading_people_to_the_database()

    # print(p_list)