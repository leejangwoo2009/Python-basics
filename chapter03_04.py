# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언

a = ()
b = (1,) #() 생략 가능하지만 데이터가 1개일 때는 반드시 ','가 있어야 함
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1])
print('e -', e[-1][1]) #-1안의 인덱스 1 인 데이터
print('e -', list(e[-1][1])) #리스트로 형변환 > 불변 특징이 없어짐

# 수정x
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d -', d[0:3]) # 3-1 = 2에따른 0,1,2까지
print('d -', d[2:])
print('e -', e[2][1:3]) # 인덱스 0,1,2에 따른 튜플, 그 안에 인덱스1~2까지의 데이터

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자'3'이 들어간 인덱스가 뭐냐?
print('a -',  a.count(2)) # 숫자 2는 몇개냐?

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 팩킹을 나눔, () 생략 가능

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)





