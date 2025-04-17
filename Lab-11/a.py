import psycopg2
import re

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Lab 10",
    user="postgres",
    password="q2e4t6u8"
)
cur = conn.cursor()

def search_contacts(pattern):
    cur.execute("""
        SELECT * FROM phone_book
        WHERE personname ILIKE %s OR phonenumber ILIKE %s
    """, (f"%{pattern}%", f"%{pattern}%"))
    return cur.fetchall()

def insert_or_update_contact(name, number):
    cur.execute("SELECT 1 FROM phone_book WHERE personname = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE phone_book SET phonenumber = %s WHERE personname = %s", (number, name))
    else:
        cur.execute("INSERT INTO phone_book(personname, phonenumber) VALUES(%s, %s)", (name, number))
    conn.commit()

def bulk_insert_contacts(names, numbers):
    for name, number in zip(names, numbers):
        insert_or_update_contact(name, number)


def get_paginated_contacts(limit, offset):
    cur.execute("SELECT * FROM phone_book ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    return cur.fetchall()


def delete_contact_by_identifier(identifier):
    cur.execute("DELETE FROM phone_book WHERE personname = %s OR phonenumber = %s", (identifier, identifier))
    conn.commit()


if __name__ == "__main__":
    while True:
        print("""
Выберите операцию:
1. Поиск по шаблону
2. Добавить или обновить контакт
3. Массовая вставка
4. Просмотр с пагинацией
5. Удалить по имени или номеру
6. Выход
""")
        choice = input("Введите номер операции: ")

        if choice == "1":
            pattern = input("Введите шаблон для поиска: ")
            results = search_contacts(pattern)
            for row in results:
                print(row)

        elif choice == "2":
            name = input("Введите имя: ")
            number = input("Введите номер телефона: ")
            insert_or_update_contact(name, number)
            print("Контакт добавлен или обновлен.")

        elif choice == "3":
            n = int(input("Сколько контактов вы хотите добавить? "))
            names = []
            numbers = []
            for _ in range(n):
                names.append(input("Имя: "))
                numbers.append(input("Номер: "))
            invalid = bulk_insert_contacts(names, numbers)
            if invalid:
                print("Неверные данные:", invalid)
            else:
                print("Все контакты успешно добавлены.")

        elif choice == "4":
            limit = int(input("Введите лимит: "))
            offset = int(input("Введите смещение: "))
            contacts = get_paginated_contacts(limit, offset)
            for contact in contacts:
                print(contact)

        elif choice == "5":
            identifier = input("Введите имя или номер для удаления: ")
            delete_contact_by_identifier(identifier)
            print("Контакт удален.")

        elif choice == "6":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    cur.close()
    conn.close()
