import psycopg2
from config import load_config


def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, vendor_list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_vendor(vendor_name):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name, ))

                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]

            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        print(vendor_id)



insert_many_vendors([
    ('AKM Semiconductor Inc.',),
    ('Asahi Glass Co Ltd.',),
    ('Daikin Industries Ltd.',),
    ('Dynacast International Inc.',),
    ('Foster Electric Co. Ltd.',),
    ('Murata Manufacturing Co. Ltd.',)
])

insert_vendor("3M Co.")



