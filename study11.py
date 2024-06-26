# 함수
# 1. 매개변수 받고 결과를 리턴하는 형태
def fun1(name):
    return "hello" + name

# 2. 매개변수 받고 결과를 리턴하지 않는 형태
def fun2(name):
    print("hello" + name)

# 3. 매개변수 안 받고 결과를 리턴하는 형태
def fun3():
    return "hello everyone~!!"

# 4. 매개변수 안 받고 결과를 리턴하지 않는 형태
def fun4():
    print("hi bye me!")

# 함수 실행하기
result = fun1('홍길동')
print(result)
fun2('일지매')
result2 = fun3()
print(result2)
fun4()

# 내장 함수
engt = "python programming"
kot = "파이썬 프로그래밍"
pro = ["OA", "Prog", "Multi", "Prog"]
print("len:", len(engt), len(kot), len(pro))
print("count:", engt.count("p"), kot.count("파"), pro.count("Prog"))
print("index:", engt.index("h"), pro.index("OA"))
# print("index:", engt.find("h"), pro.find("OA")) # list에는 find가 없음
print(dir([]))
print("index:", engt.find("k")) # 해당 객체 없으면 -1 리턴
# print("index:", engt.index("k")) # 해당 객체 없으면 Value Error 리턴

# 문자열
prog = "java c++ Python html15"
print(prog.upper())
print(prog.lower())
print(prog.istitle())
res = prog.replace("c++", "GO")
print(res)
print(prog)

# 문자열 연결
text = "123abc가나다"
prog = ["java", "c++", "python", "html15"]
print("-".join(text))
print(", ".join(prog)) # 결과: "java, c++, python, html15

# 문자 분리
t1 = "java py html"
t2 = "java/py/html"
print(t1.split()) # 리스트 형태로 출력
print(t2.split("/"))

# 공백 제거
t = "  korea  123 "
print(len(t), t)
print(len(t.lstrip()), t.lstrip()) # 왼쪽 공백 제거
print(len(t.rstrip()), t.rstrip()) # 오른쪽 공백 제거
print(len(t.strip()), t.strip()) # 왼, 오 양쪽 공백 제거

# ord(문자), chr(숫자)
for a in range(65, 91):
    print(chr(a), end = "") # 숫자에 해당하는 문자 출력 (아스키코드)

# 숫자 함수
print(abs(-3))
print(pow(3, 4), 3 ** 4) # pow(숫자, 앞 숫자를 몇 번 제곱)
print(max(5, 2, 4, 8, 3)) # () 이 안의 수들 중에 가장 큰 수
print(min(5, 2, 4, 8, 3)) # () 이 안의 수들 중에 가장 작은 수
print(round(3.147)) # 반올림, 정수만 출력
print(round(3.547)) # 반올림, 정수만 출력
print(round(3.147, 2)) # round(반올림할 숫자, 반올림한 숫자의 소수점자리) 출력

# 진법 - bin(), oct(), hex() 로 변환한 결과는 str
x = 35
b, o, h = bin(x), oct(x), hex(x) # 2진, 8진, 16진
print(b, o, h)
print(type(b), type(o), type(h), sep = "\n")

# int("진법형태값", 진법수) => 10진수
print(int("0b11", 2), int("11", 2)) # 결과: 3, 3
print(int("0o11", 8), int("11", 8)) # 결과: 9, 9
print(int("0x11", 16), int("11", 16)) # 결과: 17, 17

# math 라이브러리
import math
print(math.pi) # 파이
print(math.e)
print(math.trunc(1.78)) # 소수점 아래 버림, 결과: 1
print(math.factorial(5)) # 5x4x3x2x1, 결과: 120
print(math.degrees(math.pi))
print(math.radians(180))
print(math.sin(math.pi / 2))
print(math.cos(math.pi / 2))
print(math.log10(100))
print(math.log2(8))
print(math.pow(3, 4))

# random
import random as r
print(r.random())
print(r.randint(10, 20)) # 10 이상 20 이하 범위의 랜덤한 숫자
print(r.randrange(10, 20)) # 10 이상 20 미만 범위의 랜덤한 숫자

# 날짜 / 시간 함수
import time
print(time.time()) # 1970년 1월 1일 0시 0분 지난 초단위
print(time.localtime(time.time()))

import time
t = time.localtime(time.time())
print(f"{t.tm_year}-{t.tm_mon}-{t.tm_mday}")
print(time.strftime("%Y-%m-%d", t))

import datetime
now = datetime.datetime.today()
print(datetime.datetime.today())
print(datetime.datetime.now())
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.strftime("%Y-%m-%d (%a)"))
print(now.strftime("%H-%M-%S"))

# 반환 값이 여러 개인 경우
def calc(a, b):
    return a + b, a - b, a * b
res1, res2, res3 = calc(2, 3)
print(res1, res2, res3)
res4 = calc(2, 3)
print(res4)

# 가변 인수를 받는 함수
def data_sum(*n):
    s = 0
    print(type(n))
    for i in n:
        s += i
    return s

print(data_sum(1))
print(data_sum(1, 2))
print(data_sum(1), 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_kwargs(a = 1) # {"a":1}
print_kwargs(name = "foo", age = 3) # {"name":"foo", "age":3}

# return - 금칙어
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다."%nick)

say_nick("아이돌")
say_nick("바보")

# 매개변수에 초기값 미리 설정
def say_myself(name, age, man = True): # 변수 값을 default로 초기화
    print("나의 이름은 %s"%name)
    print("나이는 %d살입니다."%age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('홍길동',18,True)
say_myself('임꺽정',18) # default가 True임
say_myself("유관순",20,False)

# 매개변수 중 default로 초기화 된 매개변수는 가장 나중에 위치함
# def say_myself2(name, man=True, age): # 변수값을 default로 초기화
#     print("나의 이름은 %s"%name)
#     print("나이는 %d살입니다"%age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# 함수 안에서 선언한 변수의 효력범위(scope)
a = 1
def vartest(a): # 변수내 / 변수의 매개변수부에서 선언된 변수는 함수 내에서만 사용
    a = a + 1

vartest(a)
print(a)

# return
a = 1
def vartest2(a): # 변수내 / 변수의 매개변수부에서 선언된 변수는 함수 내에서만 사용
    a = a + 1
    return a

a = vartest2(a)
print(a)

a = 1
def vartest3(): # 변수내 / 변수의 매개변수부에서 선언된 변수는 함수 내에서만 사용
    global a
    a = a + 1

vartest3()
print(a)

# 재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

import math
print(math.factorial(5))