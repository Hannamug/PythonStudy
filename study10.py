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

# 퀴즈: 리스트를 아래와 같이 dict_bleed{}로 변환하시오.
# blist = ['A', 'O', 'B', 'AB', 'B', 'A', 'AB', 'AB', 'A', 'A']
# dict_bleed = {}
# # {'A':4, 'B':2, 'AB':3, 'O':1}
# for x in blist:
#     dict_bleed[x] = blist.count(x)
# print(dict_bleed)