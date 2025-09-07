# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = ''''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1,), len(str1_t1))
print(type(str2_t2,), len(str2_t2))

# 이스케이프 문자 사용

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
# I'm Boy

print("I'm Boy")
print('I\'m boy')
print('a \t b') # 자주 사용
print('a \n b') # 자주 사용
print('a \"\" b')

escape_str1 = "Do you have a \"retro game\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력
raw_s = r'D:\tpython\test'
print(raw_s)
print()


# 멀티라인 입력
#역슬러시 사용
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)

# 문자열 연산 > 많이 씀
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "Howe are you doing?"
str_o4 = "Seoul!Daejeon!Busan!Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # str_o1에 y가 있어?
print('n' in str_o1)
print('P' not in str_o2) # 대소문자 구분함, 없냐고 물어서 없다고 True
print('P' in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize : ", str_o1.capitalize()) # 첫번째 시작 글자를 대문자로 변환
print("endswith? : ", str_o2.endswith("!")) # 마지막 글자가 뭔지 체크
print("replace", str_o1.replace("thon", " Good")) # 대체하는 것
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split("!"))

#  반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__ 이 있다면 반복 가능

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"#-로 거꾸로 인덱스는 -1부터 시작

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) # [5:11]
print(str_s1[:len(str_s1)]) # str_s1[:11}
print(str_s1[:len(str_s1)-1]) # str_s1[:10}
print(str_s1[1:9:2])# 인덱스 0~9까지, 인덱스 1을 가지고 오고 2-1만큼 건너뒨 문자
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2]) # 처음과 끝, 2-1칸 간격을 두고 가지고 와라
print(str_s1[::-1]) # 거꾸로

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로


























