# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True))# 0이 아닌 수 'abc', [1, 2, 3....], (1, 2, 3....),{1, 2, 3}
print(type(False)) # 0, "", [], {}

# 예1
if True:
    print('Good')

if False:
    print('Bad')

# 예2
if True:
    print('Bad!')
else:
    print('Good!')

print()

# 관계 연산자
# >, >=, <, <=< == <!=
x = 15
y = 10

# 양변이 같은 경우 참
print(x == y)

# 양변이 다를 경우 참
print(x != y)

# 왼쪽이 클때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

print()

# 예제3
city =''
if city:
    print('Your are in :', city)
else:
    print('plz enter your city')
print()

# 예제4
city2 ='Seoul'
if city2:
    print('Your are in :', city2)
else:
    print('plz enter city')
print()

# 논리 연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b> c) # a > b > c
print('or:', a > b or b > c) # 앞이 맞으면 뒤는 실행 안됨
print('not:', not a > b)
print('not:', not b > c)
print(not True)
print(not False)
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 :', 3 + 12 > 7 + 3)
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and 7 + 3 == 10) # and는 둘다 True여야 참을 반환
print()

# 예4
score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()

# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')
print()

# 예6
# 다중조건문

num = 75

if num >= 90:
    print('Grade :', 'A')
elif num >= 80:
    print('Grade :', 'B')
elif num >= 70:
    print('Grade :', 'C')
elif num >=60:
    print('Grade :', 'D')
else:
    print('Grade :', '낙제')

print()

# 예7
# 중첩 조건문

grade = 'A'
total = 88

if grade == 'A':
    if total > 90:
        print('장학금 : 100%')
    elif total >= 80:
        print('장학금 : 90%')
    else:
        print('장학금 : 80%')
else:
    print('장학금 없음')
print()

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {'name' : 'Lee', 'city' : 'Seoul', 'grade' : 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values()) #values라고 정해주지 않으면 기본으로 키만 있는지 봄 



























