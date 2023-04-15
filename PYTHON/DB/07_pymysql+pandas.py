import pymysql
import pandas as pd

host_name = 'localhost'
host_port = 3306
username = 'root'
password = 'wjddms4120**'
database_name = 'student_mgmt'

db = pymysql.connect(
    host= host_name,
    port= host_port,
    user= username,
    passwd= password,
    db= database_name,
    charset= 'utf8'
)

SQL = "SELECT * FROM students"

df = pd.read_sql(SQL, db)

df.to_csv('students.csv', sep=',', index=False, encoding='utf-8')