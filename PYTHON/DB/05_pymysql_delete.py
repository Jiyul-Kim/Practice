import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')
cursor = db.cursor()

sql = """
DELETE FROM product
WHERE PRODUCT_CODE = '638171507675732772'
"""
cursor.execute(sql)

db.commit()
db.close()