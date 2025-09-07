# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복 o, 수정o, 삭제o)

# 선언
a =[]
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]


# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e -', list(e[-1][1]))# -1번째 리스트에 0,1번째 인덱스인 Base

# 슬라이싱
print('>>>>>>')
print('d -', d[0:3]) # 3-1
print('d -', d[2:]) # 0, 1, 2를 제외하고 다 나와라
print('e -', e[-1][1:3]) # -1 뒤에서 1번째 리스트를 가지고 오고 그 안에 0,1번째와 3-1번째 인덱스 데이터를 가지고 와라

# 리스트 연산, 집합 + 집합과 같음
print('>>>>>>')
print('c + d', c+d)
print('c * 3', c*3) # 리스트를 연산하면 리스트가 나온다.
print("'Test' + c[0]", 'Test' + str(c[0])) # 형 변환을 해줘야 실행 가능함

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4 # 리스트 수정 70 > 4로 수정됨
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # C 인덱스 1과 2-1, 즉 C리스트 인덱스 1에 ['a', 'b', 'c']를 삽입 / [[]]중복 괄호일 때!
print('c - ', c)
c[1] = ['a', 'b', 'c'] # []차이점 있음!
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a -', a)
a. append(10) # 마지막 끝부분에 추가 append
print('a -', a)
a. sort() # 오름 차순 정리
print('a -', a)
a. reverse() # 역순 정리
print('a - ', a)
print('a -', a.index(3), a[3]) #인덱스 3에 해당하는 데이터를 가지고 와라
a. insert(2, 7) #위치를 인덱스로 주고 넣을 데이터를 넣기
print('a - ', a)
a. reverse()
print('a -', a)
# del a[6]
a. remove(10) #'10'이라는 데이터를 삭제 > 데이터가 많을 때 del을 쓰면 인텍스를 일일이 count해서 확인해야됨
print('a -', a)
print('a - ', a.pop()) # 제일 끝에 있는 데이터를 꺼내기
print('a -', a)
print('a - ', a.pop()) # 제일 끝에 있는 데이터를 꺼내기
print('a -', a)
print('a -', a.count(4)) # 4가 있는지 확인하여 갯수
ex = [8, 9]
a. extend(ex) # 뒤에 8,9를 추가하기
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop() # 뒤에서 부터 시작
    print(data)






