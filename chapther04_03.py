# Chapter 04-3
# 파이썬 반복문
# While 실습
# if 중첩
# while <expr>:
#       <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1
print()

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop()) #pop은 last in, last out
print()

# 예제3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')
print()

# if 중첩
# 예제 5
i = 1

while i <= 10:
    print('i:', i)
    if i ==6:
        break
    i += 1
print()
# While - else 구분

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')
print()

# 예제 7
a = ['foo', 'bar', 'baz', 'qar']
s = 'foo'

i = 0

while i < len(a): #  = 4보다 작은
        if a[i] == s: # a 리스트안의 인덱스 0,1,2,3중에 s = qux와 같은 인덱스가 있냐
            break
        i += 1 # 인덱스가 0,1,2,3까지 증가하면서 루프
else:
    print(s, 'not found in list.')
print()

# 무한 반복
# while Ture:
#       print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']

while True:
    if not a: # = False일 때
        break
    print(a.pop())