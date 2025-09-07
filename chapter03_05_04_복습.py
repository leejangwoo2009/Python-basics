# Chapter 03-04
# 파이선 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) 불변

# 선언

a = ()
b = (1,) #생략 가능하지만 데이터가 1개일 때는 반드시 ','가 있어야 함
c = (11, 12, 13 ,14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])#-1안의 인덱스 1인 데이터
print('e -', list(e[-1][1]))# 리스트로 형변환 > 불변 특징 없어짐

# 수정x
# d[0] =1500

# 슬라이싱
print('>>>>>')
print('d -', d[0:3])# 3-1 = 2에 따른 인덱스 0,1,2까지의 값
print('d - ', d[2:])
print('e - ', e[2][1:3]) # 인덱스 0,1,2에 따른 튜플, 그 안에 인덱스1~2까지의 데이터

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3)) # 숫자'3'이 들어간 인덱스가 뭐냐?
print('a -', a.count(2)) # 숫자 2는 몇개냐?

# 팩킹 & 언팩킹(Packing and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t #팩킹을 나눔, () 생략 가능

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

#팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언 > 많은 방법이 있음
a = {'name' : 'Kim', 'phone' : '01071116136', 'birth' : '871005'} # 키와 벨류값으로 이루어져 있음
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Ulsan',
    'Age' : 39,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Ulsan'),
    ('Age', 39),
    ('Grade', 'A'),
    ('Staus', True)
])
f = dict(# 제일 편함
    name = 'Niceman',
    City = 'Ulsan',
    Age = 39,
    Grade = 'A',
    Status = True
)

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

# 출력
print('a -', a['name']) #키가 존재하지 않으면 -> 에러 발생
print('a -', a.get('name1')) # 없을 경우를 대비해서 get으로 가지고 오면 error가 나지 않고 None으로 처리
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))

# 딕셔너리 추가
a['address'] ='seoul'#seoul로 변경
print('a -', a)
a['rank'] = [1, 2, 3] #아에 추가
print('a -', a)

# 딕셔너리 길이(갯수)
print('a -', len(a)) #키와 밸류 1쌍의 개수를 의미
print('b -', len(b))
print('c -', len(c))
print('d -', len(d))

# dict_keys, dict_values, dict_item : 반복문(__iter__)에서 사용 가능

print('a -', a.keys()) #키값들만 가지고옴
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())

print('a -', list(a.keys()))#키를 리스트 형태로 형변환
print('b -', list(b.keys()))

print()

print('a -', list(a.values())) #values 값들만 가지고 옴
print('b -', list(b.values()))
print('c -', list(c.values()))

print('a -', list(a.values())) #values를 리스트 형태로 형변환
print('b -', list(b.values()))

print()

print('a -', a.items()) #items를 리스트 형태로 형변환
print('b -', list(b.items()))

print()

print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)
print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)
print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)
print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)
print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)

print()

print('a -', 'birth' in a) #a안에 ''의 내용을 서치
print('a -', 'city' in a) #대소문자 구별할 것

# 추가 & 수정
a['test'] = 'test_dict' #추가됨
print('a -', a)

a['address'] = 'dj' #워래 address라는 키가 있으면 value를 dj로 수정
print('a -', a)

a.update(birth='871015') #update로 수정 가능
print('a -', a)

temp = {'address' : 'Busan'} #temp로 따로 딕셔너리 선언
a.update(temp) #update로도 수정 가능
print('a -', a)













