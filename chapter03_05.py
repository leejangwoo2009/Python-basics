# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언 > 많은 방법이 있음
a = {'name' : 'Kim', 'phone' : '01071116136', 'birth' : '871005'} # 키와 밸류값으로 이루어져있다.
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
    ('Status' , True)
])

f = dict( # 제일 편함
    Name = 'Niceman',
    City = 'Ulsan',
    Age = 39,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a -', a['name']) #키가 존재하지 않으면 -> 에러 발생
print('a -', a.get('name1')) # 없을 경우를 대비해서 get으로 가지고 오면 error가 나지 않고 None으로 처리
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이(갯수)
print('a - ', len(a)) #키와 밸류 1쌍의 개수를 의미
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_item : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys()) #키값들만 가지고 옴
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a -', list(a.keys())) #키를 리스트 형태로 형변환
print('b -', list(b.keys()))

print()

print('a - ', a.values()) #values 값들만 가지고 옴
print('b - ', b.values())
print('c - ', c.values())

print('a -', list(a.values())) #values를 리스트 형태로 형변환
print('b -', list(b.values()))

print()

print('a - ', a.items()) #values 값들만 가지고 옴
print('b - ', b.items())
print('c - ', c.items())

print('a -', list(a.items())) #items를 리스트 형태로 형변환
print('b -', list(b.items()))

print()

print('a - ', a.pop('name')) # 해당 value를 꺼내온 다음 제거
print('a - ', a)

print('c - ', c.pop('arr')) # 해당 value를 꺼내온 다음 제거
print('c - ', c)

print()

print('f -', f.popitem()) # 제일 뒷 순서부터 키와 value들을 꺼내온 다음 제거
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)

print()

print('a - ', 'birth' in a) # a안에 ''안의 키를 서치
print('a - ', 'city' in a)

# 추가 & 수정
a['test'] = 'test_dict' #추가됨
print('a - ', a)

a['address'] = 'dj'# 'address'라는 키가 있고 원래의 value를 dj로 수정
print('a- ', a)

a.update(birth='910904')# update로도 수정 가능
print('a -', a)

temp = {'address' : 'Busan'} # temp라고 따로 딕셔너리 선언 후
a.update(temp)# update로도 수정 가능
print('a -', a)















