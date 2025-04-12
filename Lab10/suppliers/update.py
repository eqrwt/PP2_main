import psycopg2

from config import load_config

def update_vendor(vendor_name, vendor_id):

    sql = """ UPDATE vendors SET vendor_name = %s WHERE vendor_id = %s """

    updated_row_count = 0

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name, vendor_id))

                updated_row_count = cur.rowcount
            
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        print(updated_row_count)
update_vendor("KCell Cooparation", 19)

