import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='bestproducts2', charset='utf8')
cursor = db.cursor()

sql = "DELETE TABEL ranking"
cursor.execute(sql)

sql = "DELETE TABEL items"
cursor.execute(sql)

db.commit()
db.close()