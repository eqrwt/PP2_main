import psycopg2
from config import load_config
import csv

def insert_from_csv(file_path):
    params = load_config()
    sql = "INSERT INTO phonebook (username, phone) VALUES (%s, %s)"
    try: 
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cur.execute(sql, (row["username"], row["phone"]))
            
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)

def insert_input():
    params = load_config()

    username = input("Enter Username: ")
    phone = input("Enter Phone: ")

    sql = "INSERT INTO phonebook (username, phone) VALUES (%s, %s)"
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (username, phone))
        
        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)







