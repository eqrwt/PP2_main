import psycopg2
from config import load_config

def update_phone(id, new_username=None, new_phone=None):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                if new_username:
                    cur.execute("UPDATE phonebook SET username=%s WHERE id=%s", (new_username, id))
                if new_phone:
                    cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (new_phone, id))
        
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("!!ERROR: !!", error)
    


    

