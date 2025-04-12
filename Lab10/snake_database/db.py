import psycopg2
from config import load_config

def get_user(username):
    params = load_config()
    sql = "SELECT id FROM users WHERE username=%s"
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username,))

                user = cur.fetchone()
                if not user:
                    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                    user = cur.fetchone()
            
            conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
    return user[0]

def get_last_score(user_id):
    params = load_config()
    sql = """ SELECT score, level FROM user_scores WHERE user_id=%s 
        ORDER BY created_at DESC"""
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_id, ))

                result = cur.fetchone()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
    return result if result else (0, 1)
    
def save_score(user_id, score, level):
    params = load_config()
    sql = """INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)"""
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_id, score, level))
            
            conn.commit()
            
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


