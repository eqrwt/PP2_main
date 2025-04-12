import psycopg2
from config import load_config

def search_phonebook(keyword):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                query = """ 
                SELECT * FROM phonebook 
                WHERE username ILIKE %s OR phone ILIKE %s
                """
                cur.execute(query, (f'%{keyword}%', f'%{keyword}%'))

                rows = cur.fetchall()
                for row in rows:
                    print(row)
                
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)


