import pymysql
from preferenceclass import Preference as preference

def read_preference_database():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    cursor.execute('SELECT PreferenceID, First_Name, Last_Name, Fav_Drink from Preference') 
    rows = cursor.fetchall()
    p_dict = {}
    for row in rows:

        f_name = row[1]
        l_name = row[2] 
        fullname = " ".join((f_name, l_name))   
        fav_drink = row[3]
        p_dict[fullname] = fav_drink 
    
    return p_dict

    cursor.close()
    connection.close()

# if __name__ == "__main__":
    read_preference_database()
    # preference_dict = read_preference_database()
    # print(preference_dict)

def uploading_preference_to_the_database(First_Name, Last_Name, Fav_Drink, Age_limit):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()

    mysql = "INSERT INTO Preference (First_Name, Last_Name, Fav_Drink, Age_limit) VALUES ('{}', '{}', '{}', {})". format(First_Name, Last_Name, Fav_Drink, Age_limit)
    cursor.execute(mysql)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    uploading_preference_to_the_database()


