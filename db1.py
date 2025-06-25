# db1.py
import sqlite3

#연결객체를 생성
# con = sqlite3.connect(":memory:")   
con = sqlite3.connect("c:\\work\\sample.db") 

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS person" +
            "(id integer PRIMARY KEY autoincrement, name TEXT, phoneNum text);")
cur.execute("INSERT INTO person (name, phoneNum) VALUES (?, ?);", 
            ("홍길동", "010-1234-5678"))

#입력 파라미터 처리 
name = "전우치"
phoneNum = "010-9876-5432"
cur.execute("INSERT INTO person (name, phoneNum) VALUES (?, ?);", (name, phoneNum))

datalist = (("이순신", "010-1111-2222"),
            ("강감찬", "010-3333-4444"),
            ("세종대왕", "010-5555-6666"))
cur.executemany("INSERT INTO person (name, phoneNum) VALUES (?, ?);", datalist)

#완료하고 종료 
con.commit()    

# cur.execute("sELECT * FROM person")
# for row in cur:
#     print(row)

# print("---fetchone()---")
# print(cur.fetchone())  # 첫 번째 행을 가져옴

# print("---fetchmany(2)---")
# print(cur.fetchmany(2))  # 다음 두 행을 가져옴  

print("---fetchall()---")
print(cur.fetchall())  # 나머지 모든 행을 가져옴

