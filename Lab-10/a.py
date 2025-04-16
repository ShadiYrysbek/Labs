import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Lab 10",
    user="postgres",
    password="q2e4t6u8"
)

cur = conn.cursor()

def inputData():
    name = input("Hello, input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO phone_book("personname", "phonenumber") VALUES(%s, %s);', (name, number))

def importFromCSV():
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO phone_book("personname", "phonenumber") VALUES(%s, %s);', (personName, phoneNumber))

def update_contact(personName, phoneNumber):
    cur.execute('UPDATE phone_book SET "phonenumber" = %s WHERE "personname" = %s;', (phoneNumber, personName))

def queryData():
    cur.execute('SELECT * FROM phone_book;')
    data = cur.fetchall()
    path = r"C:/Users/yrysb/Desktop/Labs/Lab-10/queredData.txt"
    with open(path, "w") as f:
        for row in data:
            f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")

def deleteData():
    print("Which name do you want to delete?")
    personName = input()
    cur.execute('DELETE FROM phone_book WHERE "personname" = %s;', (personName,))

def deleteAllData():
    cur.execute('DELETE FROM phone_book;')

done = False
while not done:
    print("Что вы хотите сделать?\n"
        "1. Ввести данные c консоли\n"
        "2. Загрузить данные из CSV файла\n"
        "3. Обновить существующий контакт\n"
        "4. Вывести данные из таблицы\n"
        "5. Удалить контакт по имени\n"
        "6. Удалить все данные из таблицы\n"
        "7. Выход")
    x = int(input("Enter number 1-7: "))
    if x == 1:
        inputData()
    elif x == 2:
        importFromCSV()
    elif x == 3:
        print("Enter name and new number: ")
        name = input("Name: ")
        newNumber = input("New number: ")
        update_contact(name, newNumber)
    elif x == 4:
        queryData()
    elif x == 5:
        deleteData()
    elif x == 6:
        deleteAllData()
    elif x == 7:
        done = True
    conn.commit()
    
cur.close()
conn.close()