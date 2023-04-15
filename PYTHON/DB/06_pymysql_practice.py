import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='ecommerce', charset='utf8')
cursor = db.cursor()

# Table 생성
table = """
    CREATE TABLE CPU(
        id int unsigned not null auto_increment,
        name varchar(50) not null,
        model_num varchar(20) not null,
        model_type varchar(20) not null,
        primary key(id)        
    );
"""
cursor.execute(table)

# 1 ~ 10위 아이템들 튜플 형태로 넣어서 for 문으로 한 번에 들어가게함. INSERT쓸 때 변수를 계속 추가해주지 않도록
items = ("""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '12400F', '엘더레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '13400F', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i7', '13700KF', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '13600K', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i7', '137400F', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '12400', '엘더레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i7', '13700K', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i9', '13900K', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '13500', '랩터레이크'
);
""",
"""
INSERT INTO CPU (name, model_num, model_type) VALUES (
    'i5', '13600KF', '랩터레이크'
);
""")

for item in items:
    cursor.execute(item)


# id 2 item 삭제
delete = "DELETE FROM CPU WHERE id = '2';"
cursor.execute(delete)


db.commit()
db.close()