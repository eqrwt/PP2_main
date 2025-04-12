import psycopg2
from config import load_config

def add_part(part_name, vendor_name):
    params = load_config()

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_new_part(%s, %s)", (part_name, vendor_name))

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

add_part('Lithium Battery', 'Panasonic')

