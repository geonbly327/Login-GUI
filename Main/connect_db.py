import pymysql
import mysql_user_info

_user = mysql_user_info.user_info

def fetch():
    with pymysql.connect(db=_user["db"], host=_user["host"], user=_user["user"], passwd=_user["passwd"], port=_user["port"], charset=_user["charset"]) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = "SELECT * FROM user"
            cur.execute(sql)
            db.commit()
            data = cur.fetchall()

    return data

if __name__ == "__main__":
    data = fetch()
    print(data)