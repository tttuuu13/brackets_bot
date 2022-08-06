import psycopg2
import os


#url = "postgres://tpnpnvirmmyhqd:bdff77e49f90f2ded0f6fec8816cfa43d51a44718447bb2cbacd7563e1d62ccb@ec2-34-242-8-97.eu-west-1.compute.amazonaws.com:5432/df91plvkksqs18"
url = os.environ['DATABASE_URL']

def add_user(id, name, wordType, redLetters, evenLetters):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""INSERT INTO users (id, name, wordType, redLetters, evenLetters)
                       VALUES (%s, %s, %s, %s, %s);""",
                       (id, name, wordType, redLetters, evenLetters))
    conn.close()
    cur.close()
    return True

def delete_user(name):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""DELETE FROM users WHERE name = %s;""", (name,))
    conn.close()
    cur.close()
    return True

def get_info(id):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users WHERE id = %s""", (id,))
    r = cur.fetchone()
    conn.close()
    cur.close()
    return r

def change_wordType(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET wordType = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def change_redLetters(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET redLetters = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def get_users_list():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT name from users;""")
    r = []
    for tuple in cur.fetchall():
        r.append(tuple[0])
    conn.close()
    cur.close()
    return r

def get_ids():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT id from users;""")
    r = []
    for tuple in cur.fetchall():
        r.append(tuple[0])
    conn.close()
    cur.close()
    return r

def change_evenLetters(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET evenLetters = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True






















