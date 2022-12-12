import pymysql
from pymysql import cursors
import mysql_user_info

_user = mysql_user_info.user_info

def fetch():
    with pymysql.connect(db=_user["db"], host=_user["host"], user=_user["user"], passwd=_user["passwd"], port=_user["port"], charset=_user["charset"]) as db:
        with db.cursor(cursors.DictCursor) as cur:
            sql = "SELECT * FROM user"
            cur.execute(sql)
            db.commit()
            data = cur.fetchall()

    return data

def insert(id, pw, salt):
    with pymysql.connect(db=_user["db"], host=_user["host"], user=_user["user"], passwd=_user["passwd"], port=_user["port"], charset=_user["charset"]) as db:
        with db.cursor(cursors.DictCursor) as cur:
            sql = "INSERT INTO user (id, pw, salt) VALUES (%s, %s, %s)"
            cur.execute(sql, (id, pw, salt))
            db.commit()

def select(id):
    with pymysql.connect(db=_user["db"], host=_user["host"], user=_user["user"], passwd=_user["passwd"], port=_user["port"], charset=_user["charset"]) as db:
        with db.cursor(cursors.DictCursor) as cur:
            sql = "SELECT * FROM user where id = %s"
            cur.execute(sql, (id))
            result = cur.fetchall()

            data = []
            for i in result:
                data.append(i)

            return data

if __name__ == "__main__":
    data = fetch()
    print(data)