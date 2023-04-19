import random
import itertools

food = {'일식':['규동', '우동', '미소시루', '스시', '가츠동', '오니기리', '하이라이스', '라멘', '오코노미야끼'], 
        '한식':['김밥', '김치찌개', '쌈밥', '된장찌개', '비빔밥', '칼국수', '불고기', '떡볶이', '제육볶음'], 
        '중식':['깐풍기', '볶음면', '파육', '짜장면', '짬뽕', '마파두부', '탕수육', '토마토 달걀볶음', '고추잡채'], 
        '아시안':['팟타이', '카오 팟', '시고렝', '파인애플 볶음밥', '쌀국수', '똠얌꿍', '반미', '월남쌈', '분짜'], 
        '양식':['라자냐', '그라탱', '뇨끼', '끼슈', '프렌치 토스트', '바게트', '스파게티', '피자', '파니니']}

# people = list(input("코치의 이름을 입력해 주세요. (, 로 구분)").split(','))
people = ['토미','제임스','포코']
coach_num = len(people)
new_list = []

# 만약 코치의 수가 두 명 이하면 에러 발생
if coach_num < 2:
    print("[ERROR] 코치는 최소 2명 이상 입력해야 합니다.")
elif coach_num >= 3:
    input_list = ['우동,스시', '뇨끼,월남쌈', '마파두부,고추잡채']
    for idx in range(coach_num):
        print("{}(이)가 못 먹는 메뉴를 입력해 주세요.".format(people[idx]))
        remove_items = input_list[idx].split(',')
        for remove_item in remove_items:
            new_list.append(remove_item)
        print(new_list)

for key in food:
    if new_list in food[key]:
        food[key].remove(new_list)
keys = []
vals = [[] for i in range(len(people))]


for num1 in range(1, 6):
    key = random.choice(list(food.keys()))
    keys.append(key)
    for num2 in range(len(people)):
        val = random.choice(food[key])
        vals[num2].append(val)
weeks = ['월', '화', '수', '목', '금']
print('[구분 |', ' | '.join(weeks), ']')
print('[카테고리 |', ' | '.join(keys), ']')

for idx2 in range(len(people)):
    print('[{} |'.format(people[idx2]), ' | '.join(vals[idx2]), ']')
   

