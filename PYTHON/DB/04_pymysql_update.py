import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')
cursor = db.cursor()

sql = """
    update product set
        title = '(노마진특가/품절주의) 밀리드 롱 스커트 VB-1255', 
        org_price = 9900,
        disc_price = 32000, 
        disc_percent = 69    
        WHERE PRODUCT_CODE = '638171507675732771'
"""
cursor.execute(sql)

db.commit()
db.close()