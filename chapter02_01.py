# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조는 파일 다운받으면 있음

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python start!''')
print("""Python Start!""")

print()

# seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('web site')
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'. format('one', 'two'))

print()

# %s 사용법
#왼쪽 공백
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

#오른쪽 공백
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

#글자 채우기
print('{:_>10}'.format('nice'))

#중앙 정렬
print('{:^10}'.format('nice'))

#5글자만 절삭 '.'이 꼭 있어야 절삭됨
print('%.5s' % ('nice'))
print('%.5s' % ('python study'))

#공간은 10개지만 5개만 나오게 절삭해라
print('{:10.5}'. format('pythonstudy'))

# %d
print('%d %d' % (1,2))

# 제일 간편한 방법
print('{} {}'. format(1,2))

#총 4자리의 수에서 42가 나와라, 자리가 길다면 그냥 출력됨
print('%4d' % (42))
print('{:4d}'. format(42))

# %f
print('%f' % (3.143434343434))
print('{:f}'. format(3.143434343434))

#정수부는 6자리 > 그래서 앞에 00이 붙음, 소수부는 둘째자리까지 나옴
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'. format(3.141592653589793))