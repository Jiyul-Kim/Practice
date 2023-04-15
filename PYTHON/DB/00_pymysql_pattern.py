import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')
cursor = db.cursor()

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
cursor.execute(sql)

db.commit()
db.close()