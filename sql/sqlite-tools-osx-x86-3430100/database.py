import sqlite3


def insert_variable_into_table(url):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO content (url) VALUES (?);"""

        data = (url_min, url)
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as Error
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_sqlite_record(_id):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sql_delete_query = """DELETE from database where _id = ?"""
        cursor.execute(sql_delete_query, (_id, ))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def get_content_info(_id):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from content where id = ?"""
        cursor.execute(sql_select_query, (_id,))
        records = cursor.fetchall()
        print("Вывод ID ", id)
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Почта:", row[2])
            print("Добавлен:", row[3])
            print("Зарплата:", row[4], end="\n\n")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()