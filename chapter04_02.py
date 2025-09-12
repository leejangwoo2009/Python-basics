# Chapter04-02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#       <Loop body>

for v1 in range(10): # 0~9
    print('v1 is :', v1)

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(0, 11, 2): #0 ~ 10에서 +2만큼
    print('v3 is :', v3)

print()

# 1 ~ 1000까지의 합

sum1 = 0

for v in range(1, 1001) :
    sum1 += v #sum1 + 1

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('Your are in : ', n)
print()

# 예제2
lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print('Current number : ', n)
print()

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)
print()

# 예제4
my_info = {
    'name' : 'Lee',
    'Age' : 39,
    'City' : 'Seoul'
}

for key in my_info:
    print('key : ', my_info[key])
print()

for key in my_info.keys():
    print('key : ', my_info.get(key))
print()

for v in my_info.values():
    print('value : ', v)
print()

for v in my_info:
    print('value : ',my_info[v])

# 예제5
name ='FineAppLE'

for n in name :
    if n.isupper():# 대문자를 출력
        print(n)
    else:
        print(n.upper()) # >> 더하기 연산을 사용해서 일열로 나오게 해보기
print()

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 4:
        print('Found : 4!')
        break
    else:
        print('Not found : ', num)
print()

# continue
lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue # 위의 조건이 참이면 아래 구문 skip > bool은 출력안됨
    print('current type : ', v, type(v))
    print('muliply by 2 : ', v * 3)
    print(True *3 ) # True = 1 임
print()

# for - else 'for' 문에 else가 들어가지 않음 > if 조건관 상관 없이 break이 없으면 else가 출력됨

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 3:
        print('Found : 3')
        break
else:
    print('Not found : 3')
print()

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end=' ') # 4자리 정수로, end는 한칸 뛰우고
    print() # 한줄씩 엔터됨
print()

# 변환 예제
name2 = 'Aceman'

print('Riversed', reversed(name2)) # reversed 뒤집어서 출력
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합은 순서 없음

























