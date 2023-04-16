import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='bestproducts2', charset='utf8')
cursor = db.cursor()

sql = '''
CREATE TABLE items(
    item_code VARCHAR(30) not null PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    org_price INT NOT NULL,
    dis_price INT NOT NULL,
    dis_percent INT NOT NULL,
    provider VARCHAR(100)
);
'''
cursor.execute(sql)

sql = '''
CREATE TABLE ranking(
    num INT auto_increment not null PRIMARY KEY,
    main_category VARCHAR(50),
    sub_category VARCHAR(50),
    item_ranking TINYINT UNSIGNED,
    item_code VARCHAR(30),
    FOREIGN KEY (item_code) REFERENCES items(item_code)
);
'''
cursor.execute(sql)

db.commit()
db.close()