# Quiz 01
# 체중(kg)와 키(m)를 이용한 BMI 계산식을 이용하여 신체지수에 의한 비만 분류
# 를 출력하는 프로그램을 제작하시오.
# BMI 계산식 = 체중(kg) / 키(m)^2
# 입력: 체중(kg)을 먼저 입력한 후 키(m)를 입력한다.
# 출력: BMI 계산식에 따른 판단 결과를 출력한다.
# BMI   20미만    20이상 25미만   25이상 30미만   30이상 40미만   40이상
# 판단   저체중        정상           과체중          비만       고도비만
# kg = int(input("체중: "))
# m = float(input("키: "))
# result = kg / (m ** 2)
# if result >= 40:
#     print("고도비만")
# elif result >= 30:
#     print("비만")
# elif result >= 25:
#     print("과체중")
# elif result >= 20:
#     print("정상")
# else:
#     print("저체중")

# Quiz 02
# 로그인 처리 프로그램을 제작하시오.
# 입력: 아이디를 입력한 후 비밀번호를 입력한다.
# 출력: 아이디는 "admin", 비밀번호는 "test"를 입력했을 경우
#       "Hello"를 출력하고, 틀릴 경우 "fail"를 출력
# id = input("아이디: ")
# pw = input("비밀번호: ")
# if id == "admin" and pw == "test":
#     print("Hello")
# else:
#     print("fail")

# Quiz 03
# 로그인 처리 프로그램을 개선하려고 한다.
# 입력: 아이디를 입력한 후 비밀번호를 입력한다.
# 출력: 아이디와 비밀번호를 모두 입력한 후에 아이디는 "admin"을 입력하지 않으면
#      "wrong id"를 출력한다. 비밀번호는 "test"를 입력하면 "Hello"를 출력하고
#      그렇지 않은 경우 "wrong pw"를 출력하시오.
# id = input("아이디: ")
# pw = input("비밀번호: ")
# if id != "admin":
#     print("wrong id")
# elif pw == "test":
#     print("Hello")
# else:
#     print("wrong pw")

# Quiz 04
# 연도를 입력해서 윤년이면 1을, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 다음 조건을 모두 만족해야 한다.
# - 연도가 4로 나누어 떨어지면 윤년으로 한다.
# - 하지만 100으로 나누어 떨어지는 해는 윤년이 아니다.
# - 단, 400으로 나누어 떨어지면 윤년이다.
# year = int(input("년도: "))
# if year % 4 == 0 and year % 100 != 0:
#     print(1)
# elif year % 4 == 0 and year % 400 == 0:
#     print(1)
# elif year % 100 == 0 and year % 4 == 0:
#     print(0)
# elif year % 100 == 0 and year % 4 == 0 and year % 400 == 0:
#     print(1)
# else:
#     print(0)

# Quiz 05
# 나이를 입력해서 17, 18, 19세이면 "출입허용", 그렇지 않은 경우 "출입금지"를
# 출력하는 프로그램을 작성하시오.
# yo = int(input("나이: "))
# if yo >= 17 and yo <= 19:
#     print("출입허용")
# else:
#     print("출입금지")

# Quiz 06
# 평면 상의 좌표를 입력해서 어느 사분면에 속하는지 출력하는 프로그램을 작성
# 하시오. 단, x와 y는 0이 아닌 정수임.
# x = int(input("x 좌표: "))
# y = int(input("y 좌표: "))
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)
# else:
#     print(0)

# Quiz 07
# 삼각형 세 변의 길이를 입력하여 직각삼각형이면 1, 아니면 0을 출력하는 프로
# 그램을 작성하시오. 단, 세 변의 길이는 변의 길이에 상관없이 입력한다.
# a = int(input("a의 길이: "))
# b = int(input("b의 길이: "))
# c = int(input("c의 길이: "))
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if (a ** 2) + (b ** 2) == (c ** 2):
#     print(1)
# else:
#     print(0)
