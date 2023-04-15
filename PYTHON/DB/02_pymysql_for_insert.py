import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')

cursor = db.cursor()


for idx in range(1, 10):
    PRODUCT_CODE = 638171507675732770 + idx
        
    sql = """INSERT INTO product values (
        '""" + str(PRODUCT_CODE) + """', '여성청바지 판매1위/연청추가/하비고민 덜어주는 데님 (Made)S~2XL/스테디치즈데님', 73000 , 21900 , 70 , 'F'); """
    print(sql)
    cursor.execute(sql)


db.commit()
db.close()