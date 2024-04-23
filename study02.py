# 표준 입출력
# score = input() # 외부로부터 입력 받는 함수
# print(score)

# score = input("점수: ") # input 으로 입력 받는 결과는 문자열
# print(type(score))
# print(score)

# score = input("점수: ")
# print(score + 10) # 에러 뜨는 이유는 input 값은 문자열이기 때문
# 해결법
# 1
# score = int(input("점수: "))
# print(score + 10)
# 2
# score = input("점수: ")
# print(int(score) + 10)

# print("I can't swim") # 큰 따옴표와 작은 따옴표는 서로를 구분함
# print('"파이썬" 언어') # 굳이 큰 따옴표나 작은 따옴표를 출력하고 싶으면 이렇게 구분 지으면 됨

# print('I can\'t swim') # escape(이스케이프)문자
# print("\"파이썬\" 언어") # ''나 "", /, \ 등의 특수문자를 쓰고 싶을 때 쓰는 방법 중 하나
# print("c:\\temp\\myfile.py") # \ 이거 뒤에 쓰고 싶은 특수문자 쓰면 출력에 그대로 나옴
# print("c:/temp/myfile.py") # 이건 문제 안 됨

# 연결 연산
# print("Hello" + "Python") # concat 사용, 딱 붙음
# print("Hello", "Python") # , 사용, 공백 발생
# print("Hello""Python"" 123") # 아무것도 사용X, 딱 붙음
# print("Hello", 3) # 정상 작동
# print("Hello"3) # syntax 에러 발생, 이렇게 쓰면 안 됨
# print("Hello" + 3) # concat 에러 발생, 둘이 타입이 다름(str + int)
# print("Hello" * 3) # 정상 작동, Hello가 정수만큼 반복, * 반복 연산

# formatting 문자열
name = "홍길동"
age = 17
score = 91.35
print("이름: %s"%name) # %s 는 문자열
print("나이: %d"%age) # %d 는 정수
print("score: %f"%score) # %f 는 실수
print("이름: %s, 나이: %d, 점수: %f"%(name, age, score)) # %를 써놓고 뒤에 해당하는 값을 넣는 방식

# % 포매팅
print("[%10s]"%name) # + 는 숫자 만큼 자리 수 증가(숫자 지정 없을 시 공백 처리), 오른쪽 정렬, default
print("[%-10s]"%name) # - 는 숫자 만큼 자리 수 감소(숫자 지정 없을 시 공백 처리), 왼쪽 정렬

print("[%.1f]"%score) # .1f, 소수점 1자리
print("[%.3f]"%score) # .3f, 소수점 3자리
print("[%8.1f]"%score) # 8.1f, 전체 8자리 소수점 1자리, 오른쪽 정렬
print("[%8.3f]"%score) # 8.3f, 전체 8자리 소수점 3자리, 오른쪽 정렬
print("[%-8.1f]"%score) # -8.1f, 전체 8자리 소수점 1자리, 왼쪽 정렬
print("[%-8.3f]"%score) # -8.3f, 전체 8자리 소수점 3자리, 왼쪽 정렬