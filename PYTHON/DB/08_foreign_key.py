import pymysql
import pandas as pd

host_name = 'localhost'
host_port = 3306
username = 'root'
password = 'wjddms4120**'
database_name = 'sqlDB'


db = pymysql.connect(
    host= host_name,
    port= host_port,
    user= username,
    passwd= password,
    db= database_name,
    charset= 'utf8'
)



cursor = db.cursor()

cursor = db.cursor()
SQL_QUERY = "DELETE FROM userTbl WHERE userID = 'STJ'"
cursor.execute(SQL_QUERY)
db.commit()

SQL = "SELECT * FROM buyTbl"

df = pd.read_sql(SQL, db)
print(df)