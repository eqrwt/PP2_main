import psycopg2
from config import load_config

def delete(value):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                query = """ DELETE FROM phonebook WHERE username = %s OR phone = %s """
                cur.execute(query, (value, value))

            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)




