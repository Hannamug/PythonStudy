# 딕셔너리
# {key1:value1, key2:value2, key3:value3, ...}
# key는 중복불가, value는 중복가능
d1 = {} # 빈 딕셔너리
d2 = {"name":"홍길동",
      "email":"test1@abc.com",
      "phone":"010-1234-5678"}
d3 = dict(name = "김철수",
          email = "test2@abc.com",
          phone = "010-8765-4321")
print(type(d1), type(d2), type(d3))

# 딕셔너리 item 추가
fruits = {"a":"apple", "b":"banana"}
fruits["c"] = "carrot"
print(fruits)

# 딕셔너리에 키가 중복인 item 추가 - 최종으로 입력된 value로 대체
fruits = {"a":"apple", "b":"banana"}
fruits["b"] = "blueberry"
print(fruits)

# item의 value를 list도 가능
fruits = {"a":"apple", "b":"banana"}
fruits["c"] = ["coconut", "cherry"]
print(fruits)

# item 삭제는 del 딕셔너리[키]
fruits = {"a":"apple", "b":"banana"}
del fruits["b"]
print(fruits)

# 모든 item 삭제 clear
fruits = {"a":"apple", "b":"banana"}
fruits["c"] = ["coconut", "cherry"]
print(fruits)
fruits.clear() # 모든 요소를 삭제
print(fruits)
# 딕셔너리 내에 존재하지 않는 키 삭제 시 오류
# del fruits["k"]

# 딕셔너리 내 요소 검색
fruits = {"a":"apple", "b":"banana"}
fruits["c"] = ["coconut", "cherry"]
print(fruits)

# key in 딕셔너리 True, value in 딕셔너리 False
print("b" in fruits, "banana" in fruits)

# value 검색 - values(), keys()
fruits = {"a":"apple", "b":"banana", "c":"cherry"}
print(fruits.keys(), type(fruits.keys())) # 키 객체
print(fruits.values(), type(fruits.values())) # 밸류 객체
print(fruits.items(), type(fruits.items())) # 아이템 객체

for k, v in fruits.items():
    if v == "banana":
        print(k, ":", v)

# value 존재확인
print("banana" in fruits.values())

# 딕셔너리 합치기
# 합칠 때 중복 키가 있으면 마지막 값(value)으로 대체
f1 = {"a":"apple", "b":"banana"}
f2 = {"b":"blueberry", "c":"coconut"}
f1.update(f2)
print(f1) # 결과: 'a': 'apple', 'b': 'blueberry', 'c': 'coconut'

# 퀴즈: 리스트를 아래와 같이 dict_bleed{}로 변환하시오.
# blist = ['A', 'O', 'B', 'AB', 'B', 'A', 'AB', 'AB', 'A', 'A']
# dict_bleed = {}
# # {'A':4, 'B':2, 'AB':3, 'O':1}
# for x in blist:
#     dict_bleed[x] = blist.count(x)
# print(dict_bleed)

# 딕셔너리 정렬
# 키를 기준으로 정렬
data = {"d":8, "c":5, "a":9, "b":2}
d1 = sorted(data)
d2 = sorted(data.keys()) # 키를 오름차순으로 정렬
d3 = sorted(data.keys(), reverse = True) # 키를 내림차순으로 정렬
print(d1, d2, d3)

# 키를 기준으로 내림차순한 후 키와 값 모두 출력
data = {"d":8, "c":5, "a":9, "b":2}
d3 = sorted(data.keys(), reverse = True) # []
for k in d3:
    print(k, data[k])

# 값을 기준으로 정렬
data = {"d":8, "c":5, "a":9, "b":2}
d2 = sorted(data.values())
d3 = sorted(data.values(), reverse = True)
print(d2, d3)

# 키와 값의 쌍을 기준으로 정렬
data = {"d":8, "c":5, "a":9, "b":2}
d1 = sorted(data.items())
d2 = sorted(data.items(), reverse = True)
print(d1, d2)

# 람다식 정렬
# 키를 기준으로 정렬
data = {"d":8, "c":5, "a":9, "b":2}
k1 = sorted(data.items(), key = lambda x:x[0]) # 오름차순 정렬
k2 = sorted(data.items(), key = lambda x:x[0], reverse = True) # 내림차순 정렬
print(k1, k2)

# 값을 기준으로 정렬
data = {"d":8, "c":5, "a":9, "b":2}
v1 = sorted(data.items(), key = lambda x:x[1]) # 오름차순 정렬
v2 = sorted(data.items(), key = lambda x:x[1], reverse = True) # 내림차순 정렬
print(v1, v2)

# 값이 가장 큰 키를 출력
data = {"d":8, "c":5, "a":9, "b":2}
sdata = sorted(data.items(), key = lambda x:x[1]) # 오름차순 정렬
print(sdata[-1], sdata[-1][0], sdata[-1][1])

# 값이 가장 큰 키를 기준으로 내림차순으로 전부 출력
data = {"d":8, "c":5, "a":9, "b":2}
sdata = sorted(data.items(), key = lambda x:x[1], reverse = True) # 내림차순 정렬
for k, v in sdata:
    print(k, v)

# lambda 예약어
# 함수_이름 = lambda 매개변수, 매개변수2, ...: 표현식부분
# def 함수_이름(매개변수1, 매개변수2, ...):
#   return 값
def add(a, b):
    return a + b

result = add(4, 3)
print(result)

add = lambda a, b: a + b
result = add(3, 4)
print(result)