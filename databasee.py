import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="diplombase"
)

# при помощи этой команды можно писать запросы
# mycursor.execute("create database DiplomBase")
mycursor = db.cursor()


# просмотр баз данных
def check_DB():
    mycursor.execute("show databases")
    for x in mycursor:
        print(x)


def check_table():
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)


def create_struct_table():
    mycursor.execute(
        "create table users (first_name varchar(255), second_name varchar(255), last_name varchar(255), mail varchar(255))")

    mycursor.execute("ALTER TABLE users ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT UNIQUE)")


def inserter(user_id, first_name, second_name, last_name, mail):
    sql = "INSERT INTO users (user_id, first_name, second_name, last_name, mail) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, first_name, second_name, last_name, mail)
    mycursor.execute(sql, val)
    db.commit()


def search_user_mail(user_id):
    email = ""
    mycursor.execute(f"select mail from users where user_id = {user_id}")
    for x in mycursor:
        email = x
    return email


def search_user_FIO(user_id):
    Name = ""
    mycursor.execute(f"select first_name, second_name, last_name from users where user_id = {user_id}")
    users = mycursor.fetchall()
    for x in users:
        Name = x
    return Name


def bool_search_user_FIO(user_id):
    user = 0
    mycursor.execute(f"select count(user_id) from users where user_id = {user_id}")
    for x in mycursor:
        user += 1
    return user
