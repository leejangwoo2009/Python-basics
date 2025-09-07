# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x)

# 선언 > set & {} (키&value 형식이 아님)도 사용 가능
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'bar', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)
print()

# 튜플 형변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
print()

# 리스트 형변환(set -> list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 -', l2)
print()

# 길이(갯수)- 집합된 부분을 1개로, 중복은 제외
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2 :', s1 & s2)
print('s1 & s2 :', s1.intersection(s2))
print()

# 합집합
print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))
print()

# 차집합
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))
print()

# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2)) # False이면 중복이 있음!
print()

# 부분 집합 확인
print('subset :', s1.issubset(s2)) # s1는 s2에 부분 집합?
print('superset :', s1.issuperset(s2)) # s1은 s2의 상위 집합?
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
print()

# Remove
s1.remove(5)
print('s1 -', s1)
print()

# Discard
s1.discard(3)
print('s1 -', s1)
s1.discard(7) # 7이 없더라도 error가 나지 않음 = 예외가 발생하지 않음
print('s1 -', s1)
print()

# 모두 삭제
s1.clear()s
print('s1 - ', s1)

a =[1, 2, 3, 4, 5]
a. clear()
print('a -', a)






