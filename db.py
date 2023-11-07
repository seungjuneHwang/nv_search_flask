import sqlite3

# 데이터 넣기 함수
def save(search):
    conn = sqlite3.connect('mydb.db')
    # Cursor 객체 생성
    c = conn.cursor()

    # 테이블 생성
    # sql = "CREATE TABLE tb_search (id integer primary key autoincrement, search text)"

    # 데이터 넣기
    sql = f"INSERT INTO tb_search (search) VALUES ('{search}')"
    c.execute(sql)
        
    # execute 에 db 에 적용
    conn.commit()

    # 접속한 db 닫기
    conn.close()
    
# 데이터 찾기 함수
def find_all():
    conn = sqlite3.connect('mydb.db')
    # Cursor 객체 생성
    c = conn.cursor()

    # 데이터 불러 와서 출력
    for row in c.execute('SELECT * FROM tb_search'):
        print(row)

    # 접속한 db 닫기
    conn.close()

# 데이터 저장
# save('수능')
# # 저장된 데이터 전체 출력
# find_all()