import psycopg2
from config import load_config

#execution sql
def execute_sql_file(filename):
    params = load_config()
    with open(filename, 'r') as file:
        sql = file.read()

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
        print("SQL file executed successfully.")
    except Exception as e:
        print("Error executing SQL file:", e)

# searching
def search_phonebook(keyword):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.callproc('search_phonebook', (keyword, ))

                rows = cur.fetchall()
                for row in rows:
                    print(row)
                
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)


#quering 
def printing():
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.callproc("get_phonebook_paginated", (5, 0))

                rows = cur.fetchall()
                for row in rows:
                    print(row)
                
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)

#deleting
def delete(value):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL delete_user(%s, %s)', (value, value))

            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)
    finally:
        print(f"Deleted: {value}")

#inserting
def insert_input():
    params = load_config()

    username = input("Enter Username: ")
    phone = input("Enter Phone: ")
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:

                cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
        
        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)
    finally:
        print(f"Inserted {username}, {phone}")

execute_sql_file("logic.sql")
printing()
insert_input()
printing()




