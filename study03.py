# format 메소드
name = "홍길동"
age = 18
score = 93.51
print("이름: {}, 나이: {}, 점수: {}".format(name, age, score)) # {} 이 안에 인덱스 순서 지정 없으면 차례대로
print("이름: {1}, 나이: {2}, 점수: {0}".format(score, name, age)) # {} 이 안에 인덱스 순서 지정대로

print("[{:>10}]".format(name)) # 벌리고 있는 방향 정렬, 오른쪽 정렬
print("[{:<10}]".format(name)) # 벌리고 있는 방향 정렬, 왼쪽 정렬
print("[{:^10}]".format(name)) # 가운데 정렬
print("[{:.5f}]".format(score)) # 소수점 5자리까지
print("[{:8.3f}]".format(score)) # 소수점 3자리까지 오른쪽 정렬, default
print("[{:<8.3f}]".format(score)) # 소수점 3자리까지 왼쪽 정렬
print("[{:>8.3f}]".format(score)) # 소수점 3자리까지 오른쪽 정렬
print("[{:,}]".format(1230000)) # 3자리마다 , 사용, default

# > 기호 앞에 문자열을 쓰면 공백을 해당 문자열로 채워줌
print("[{:*>10}]".format(name))
print("[{:#<10}]".format(name))
print("[{:?^10}]".format(name))

# 분리 후 사용
temp = "이름: {}, 나이: {}, 점수: {}"
temp = temp.format(name, age, score)
print("분리 ex)", temp)

# f 문자열
# 파이썬 3.6부터 지원
print(f"f 문자열 ex) 이름: {name}, 나이: {age}, 점수: {score}")
print(f"[{name:>10}], [{age:>10}]")
print(f"[{name:<10}], [{age:<10}]")
print(f"[{name:^10}], [{age:^10}]")

# 포맷팅으로 url 작성하기
site = "https://api.thingspeak.com/update?api_key="
apikey = "YTRUYF6Y045MOB37"
v1 = 5
v2 = 10
# 첫번째 방식
url = f"{site}{apikey}&field={v1}&field2={v2}"
print(url)
# 두번째 방식
url2 = "%s%s&field1=%d&field2=%d"%(site, apikey, v1, v2)
print(url2)
# 세번째 방식
url3 = "{}{}&field1={}&field2={}".format(site, apikey, v1, v2)
print(url3)