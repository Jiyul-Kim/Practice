# 1. 라이브러리 가져오기
import pymysql

# 2. 접속
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')

# 3. 커서 가져오기
ecommerce = db.cursor()

# 4. sql 구문 만들기
sql = """
    CREATE TABLE product(
        PRODUCT_code varchar(20) not null,
        title varchar(50) not null,
        org_price int not null,
        disc_price int not null,
        disc_percent int,
        delivery varchar(2),
        primary key(PRODUCT_code)        
    );
"""

# 5. sql 구문 실행
# 에러가 없으면 출력 값은 0
ecommerce.execute(sql)

# 6. DB에 커밋하기
# 모두 끝났다면, connect을 가지고 있는 객체가 데이터를 commit 해야함.
db.commit()

# 7. DB 연결 닫기
db.close()