import psycopg2

from config import load_config

def select_by_id(id):
    try:
        sql = "SELECT * FROM phonebook WHERE id = %s"
        params = load_config()
        with psycopg2.connect(**params) as con:
            with con.cursor() as cur:
                cur.execute(sql, (id))
                rows = cur.fetall()
                for row in rows:
                    print(row)
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)