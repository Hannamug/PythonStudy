# 연산자
# 산술, 대입, 비교, 논리, 비트

# 산술
print(2 + 3) # 더하기
print(4 / 2) # 나누기, 실수
print(7 % 3) # 나머지
print(7 // 3) # 몫
print(2 ** 3) # 제곱 2^3(세제곱 함)

a = 7
b = 3
result = f"{a}를(을) {b}(으)로 나눈 몫은 {a // b}이고, 나머지는 {a % b}입니다."
print(result)

# root 표현
print(4 ** 0.5)

# 대입 연산자 =
a = 5
a = a + 1
print(a) # 결과: 6
a += 2 # a = a + 2 라는 뜻, 결과: 8
print(a)
a -= 4 # a = a - 4 라는 뜻, 결과: 4
print(a)
# a++ # 이건 안 됨

# 비교 연산자
a = 5
b = 10
print(a > b) # a가 b보다 큰가?
print(a >= b) # a가 b보다 크거나 같은가?
print(a < b) # a가 b보다 작은가?
print(a <= b) # a가 b보다 작거나 같은가?
print(a == b) # a와 b가 같은가?
print(a != b) # a와 b가 같지 않은가?
print("-----"*10)

# 논리 연산자
# and, or, not
print(True and True) # 결과: True
print(a > 2 and b > 2) # 결과: True
print(True and False) # 결과: False
print(0 and 1) # 0 = False, 1 = True, 파이썬에선 이렇게 설정, 그래서 결과: False(= 0)
print("-----"*10)
print(True or True)
print(0 or 1) # or 이라 둘 중에 하나만 참이면 되어서 결과: True(= 1)
print(True or False)
print("-----"*10)
print(not True)
print(not False)

# 비트(bit) 연산
a = 13 # 1101 = 13
b = 10 # 1010 = 10
#   결과: 1000 = 8
#   결과: 1111 = 15
#   결과: 0111 = 7
print(a & b) # & 는 and 와 같음(비트 연산에서만 쓰임), 1000
print(a | b) # | 는 or 와 같음(비트 연산에서만 쓰임), 1111
print(a ^ b) # ^ 는 xor 와 같음(비트 연산에서만 쓰임), 0111
# &, |, ^, ~, <<, >> 들은 비트 연산자라 비트 연산 시에만 쓰임