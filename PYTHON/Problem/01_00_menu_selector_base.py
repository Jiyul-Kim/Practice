import random
import itertools

a = {'A':[1, 2, 3, 4],
     'B':[5, 6, 7, 8],
     'C':[9, 10, 11, 12]}
people = ['a', 'b', 'c', 'd']
b = 4
a_value_list = []
for key in a:
    if b in a[key]:
        a[key].remove(b)
keys = []
vals = []

for i in range(1, 6):
    # print(str(i)+'번')
    key = random.choice(list(a.keys()))
    # print(key)
    keys.append(key)
    for j in range(len(people)):
        val = random.choice(a[key])
        # print(val)
        vals.append(val)
    # print('#' * 10)
    

result = []
for i in range(len(keys)):
    item = (keys[i], tuple(vals[i*4:i*4+4]))
    result.append(item)
# print(result)

# print('월요일은, ', result[0])
# print('월요일이고 카테고리는, ', result[0][1])
weeks = ['월', '화', '수', '목', '금']
# for week in weeks:
#     # print(week)

print('[구분 |', ' | '.join(weeks), ']')
print('[카테고리 |', ' | '.join(keys), ']')

for m in range(len(people)):
    print('[{} |'.format(people[m]), ' | '.join(str(result[i][1][m]) for i in range(5)), ']')

    
print('#' * 10)
