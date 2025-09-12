# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#       <Loop body>

for v1 in range(10): #0~9까지, 무조건 n-1
    print('v1 is :', v1)
print()

for v2 in range(1, 11): # 0~ 10까지 무조건 n-1
    print('v2 is :', v2)
print()

for v3 in range(1, 11, 2): # 0~ 10까지 무조건 n-1, 2만큼의 간격
    print('v3 is :', v3)
print()

# 1 ~ 1000합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 sum :', sum1)
print('1 ~ 1000 sum :', sum(range(1, 1001)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))
print()

# iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are : ', n)
print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for e in lotto_numbers:
    print('Current number : ', e)
print()

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)
print()

# 예제4
my_info = {
    'Name' : 'Lee',
    'Age' : '39',
    'City' : 'Seoul'
}

for values in my_info:
    print('values :', my_info[values])

for v in my_info.values():
    print('values :', v)
print()





