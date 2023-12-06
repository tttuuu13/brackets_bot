import psycopg2
import os


#url = "postgres://jrqldxhxhgiblz:12b1e23556a5f16aab4d30bb704f13b1877c663ed639a7400362ae7cb3581ef9@ec2-52-50-90-145.eu-west-1.compute.amazonaws.com:5432/d5tl7oq88soio"
url = os.environ['DATABASE_URL']
price = 100

def add_premium(id, name, date, days):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    if id in get_ids():
        cur.execute(f"""DELETE FROM slovomaster WHERE id = %s;""", (id,))
    cur.execute("""INSERT INTO slovomaster (id, name, wordtype, redletters, evenletters, date, days)
                       VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                       (id, name, 'normal', True, True, date, days))
    #stats = get_stats()
    #users = int(stats[0])
    #money = int(stats[1])
    #date = stats[2]
    #cur.execute("""UPDATE money SET redLetters = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def delete_user(name):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""DELETE FROM slovomaster WHERE name = %s;""", (name,))
    conn.close()
    cur.close()
    return True

def get_info(id):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT * FROM slovomaster WHERE id = %s""", (id,))
    r = cur.fetchone()
    conn.close()
    cur.close()
    return r

def get_infos():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT * from slovomaster;""")
    r = [list(i) for i in cur.fetchall()]
    conn.close()
    cur.close()
    return r

def change_wordType(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE slovomaster SET wordType = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def change_redLetters(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE slovomaster SET redLetters = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def get_users_list():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT name from slovomaster;""")
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
    cur.execute("""SELECT id from slovomaster;""")
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
    cur.execute("""UPDATE slovomaster SET evenLetters = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True


def update_date(date):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE money SET date = %s;""", (date,))
    conn.close()
    cur.close()
    return True

def get_date():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT date FROM money;""")
    r = cur.fetchall()[0][0]
    conn.close()
    cur.close()
    return r























