import mysql.connector
from mysql.connector import Error


connection = None
cursor = None
try:
    connection = mysql.connector.connect(host="localhost", database="employeedb", user="root", password=input("Enter password:"))

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySql Server :", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("you are connected to database :", record)

        create_table_query = """create table if not exists laptop(id int not null,
        name varchar(255) not null,
        price float not null,
        purchase_date date not null,
        primary key(id))"""

        result = cursor.execute(create_table_query)
        print("Laptop table successfully created")

except Error as e:
    print("Error while connecting to MySQl", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")