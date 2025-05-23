import psycopg2
from config import load_config


def get_vendors():

    config = load_config()
    try:
        sql = "SELECT vendor_name, vendor_id FROM vendors ORDER BY vendor_name"
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                curr.execute(sql)
                print("The number of rows: ", curr.rowcount)

                row = curr.fetchone()
                while row:
                    print(row)
                    row = curr.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name;
                """)
                for row in iter_row(cur, 10):
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

get_part_vendors()
