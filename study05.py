# 제어문

# 조건문
# if 조건식:
#   실행문
# 점수를 입력받아서 80점 이상이면 "pass" 출력
# score = int(input("점수: "))
# if score >= 80:
#     print("pass")
# if score < 80:
#     print("fail")

# if ~ else
# score = int(input("점수: "))
# if score >= 80:
#     print("pass")
# else:
#     print("fail")

# if ~ elif ~ else
# score = int(input("점수: "))
# if score >= 80:
#     print("A")
# elif score >= 70: # 70~79
#     print("B")
# else: # 0~69
#     print("C")

# 90점 이상, 80점 이상, 70점 이상, 60점 이상, 60점 미만
#  A         B         C         D         F
# score = int(input("점수: "))
# if score >= 90: # 90~
#     print("A")
# elif score >= 80: # 80~89
#     print("B")
# elif score >= 70: # 70~79
#     print("C")
# elif score >= 60: # 60~69
#     print("D")
# else: # 0~59
#     print("F")

# if True인 경우 아무것도 하지 않는 문장
# card = True
# if card:
#     pass
# else:
#     print("걸어감")

# card = True
# if card: pass
# else: print("걸어감")

# 조건부 표현식
# score = int(input("점수: "))
# 변수 = 조건문이 참인 결과 if 조건문 else 조건문이 거짓인 결과
# message = "success" if score >= 60 else "failure"
# print(message)

# '23 12 45'
temp = input().split()
# temp = '23 12 45'.split()
print(temp)

a, b, c = map(int, temp) # ['23', '12', '45'] => [int('23'), int('12'), int('45')]
print(a, type(a), b, type(b), c, type(c))

for x in temp:
    print(int(x), end=' ')