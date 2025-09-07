# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : tlftn
complex : qhrthtn
bool : qnffls
str : 문자열 ( 시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""
import char

# 데이터 타입
str1 = 'Python'
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0
int_v = 7
list =[str1, str2]
dict = {
    "name" : "Machine Learning", # name이 키
    "version" : 2.0 # version이 키
}
tuple = (7, 8, 9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y), x **y -> 2**3 = pow(2,3)
"""

# 정수 선언
i = 77
i2 = -14
big_int = 789777777777777888888888888888888888889999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 789465151315849846513213216
big_int2 = 546312888481818184818188885577777
f1 = 1.234
f2 = 3.939

# +
print(">>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()

# *
print(">>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1* f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)
print()

# 형 변환 실습
a = 3.#'0' 생략 가능
b = 6
c =.7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0을 의미
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 몫 x, 나머지 y를 구하는함수 divmod

print(x,y)
print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수
print(math.pi)

#===============================================================
# Chapter03-2
# 파이썬 문자형
# 문자형 중요!

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1,), len(str1_t1))
print(type(str2_t2,), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

# I'm boy

print("I'm boy")
print('I\'m boy')
print('a \t b') # 자주 사용 tab 만큼 띄워쓰기
print('a \n b') # 자주 사용 줄바꿈
print('a \"\" b')

escape_str1 = "Do you have a \"retoro game\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# 멀티라인 입력
# 역슬러시 사용
multi_str = \
"""
String
Multi line
Test
"""
print(multi_str)

# 문자열 연산 > 많이 씀
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul!Daejeon!Busan!Jinju!"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #str_o1에 y가 있느냐?
print('n' in str_o1)
print("P" not in str_o2) # 대소문자 구분함, 없냐고 물어서 없으면 True
print('p' in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print('Capitalize : ', str_o1.capitalize()) # 첫번째 시작 글자를 대문자로 변환
print('endswith? : ', str_o2.endswith('!')) # 마지막 글자가 뭔지 체크
print("replace", str_o1.replace('thon', 'Good')) # 대체하는 것
print('sorted : ', sorted(str_o1))
print('split : ', str_o4.split('!'))

# 반복(시퀀스)
im_str = 'Good Boy!'

print(dir(im_str)) #__iter__이 있다면 반복 가능

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python" #-로 거꾸로 인덱스는 -1부터 시작

# 슬라이싱 연습
print(str_s1[0:3]) #0 1 2
print(str_s1[5:]) # [5:11]
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1)-1]) # str_s1[:10]
print(str_s1[1:9:2]) # 인덱스 0~9까지, 인덱스 1을 가지고 오고 2-1만큼 건너뛴 문자
print(str_s1[5:])
print(str_s1[1:-2])
print(str_s1[::2]) # 처음과 끝, 2-1칸 간격을 두고 가지고 와라
print(str_s1[::-1]) # 거꾸로

#아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) #아스키 코드로
print(char(122))










