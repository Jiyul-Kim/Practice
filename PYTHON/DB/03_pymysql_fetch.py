import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')
cursor = db.cursor()
sql = " SELECT * FROM product "
cursor.execute(sql)
result = cursor.fetchall()

for record in result:
    print(record)

db.close()