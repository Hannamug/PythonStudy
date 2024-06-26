# 리스트
# f = [] # 빈 리스트
# a = [90, 92, 84, 88, 74] # 표기법 []
# b = list((90, 92,84,88, 74)) # list() 함수
# c = ["파이썬", [900, 30.5, "자바"], 850, 78.75]
# d = list(("파이썬", 900, 30.5, "자바", 850, 78.75))
# e = list("프로그래밍") # 문자열 -> 리스트
# print(a, b, c, d, e, f, sep="\n")

# 인덱싱(해당 index의 값 추출)
# 슬라이싱(특정 index 범위의 값 추출)
# a = [90, 91, 92, 93, 94, 95, 96]
# a = list(range(90, 97))
# print(a[0]) # [0, 1, 2, 3, 4, 5, 6] [0, ..., len-1] 왼쪽부터 오른쪽으로 ->
# print(a[-1]) # [-7, -6, -5, -4, -3, -2, -1] [-len, ..., -1] 오른쪽부터 왼쪽으로 <-
# print(a[-7])

#
# a = [0, 1, 2, 3, 4, 5, 6]
# print(a[0:3]) # 0번부터 3 - 1(2) 번까지, 결과: 0, 1, 2
# print(a[3:5]) # 3번부터 5 - 1(4) 번까지, 결과: 3, 4
# print(a[0:]) # 0번부터 끝길이(전체) 까지, 결과: 0, 1, 2, 3, 4, 5, 6
# print(a[:]) # 딱히 지정하지 않으면 첫번째부터 끝길이(전체)까지, 결과: 0, 1, 2, 3, 4, 5, 6
# print(a[3:]) # 3번부터 끌깉이(전체) 까지, 결과: 3, 4, 5, 6

# a[시작:끝:증분]
# print(a[1:5:2]) # 1번부터 5 - 1(4) 번까지 2씩 증가시킨 수만, 결과: 1, 3
# print(a[::2]) # 전체 인덱스, 0번부터 끝까지 2씩 증가시킨 수만, 결과: 0, 2, 4, 6
# print(a[1::2]) # 1번부터 끝길이(전체)까지 2씩 증가시킨 수만, 결과: 1, 3, 5
# print(a[-4:-2]) # -4(3) 번부터 -2 - 1(-3 = 4) 번까지, 결과: 3, 4
# print(a[-4:]) # -4(3) 번부터 끝길이(전체)까지, 결과: 3, 4, 5, 6
# print(a[100]) # 범위를 벗어난 indexing
#     IndexError: list index out of range
# print(a[5:100]) # 해당 index 범위까지만 출력, 결과: 5, 6

# 문자열 indexing
# ct = '프로그래밍' # 인덱스 순서 ct = [(0, -5 = 프), (1, -4 = 로), (2, -3 = 그), (3, -2 = 래), (4, -1 = 밍)]
# print(ct[1], ct[-1]) # 결과: 로, 밍

# 리스트 연산 - 항목수정
# prog = ["C", "PYTHON", "JAVA", "GO"]
# prog[0] = "C++"
# print(prog)

# 리스트 복사
# prog = ["C", "PYTHON", "JAVA"]
# myprog = prog
# print("prog", prog)
# print("myprog", myprog)
# prog[0] = "C++"
# print("prog", prog)
# print("myprog", myprog)

# 깊은 복사(deep copy)
# prog = ["C", "PYTHON", "JAVA"]
# myprog = []
# for a in prog:
#     myprog.append(a)
# myprog = [a for a in prog]
# print("prog", prog)
# print("myprog", myprog)
# prog[0] = "C++"
# print("prog", prog)
# print("myprog", myprog)

# 리스트 연산
# prog = ["C", "PYTHON", "JAVA", "GO"]
# webp = ["PHP", "JSP", "ASP.NET"]
# myprog = prog + webp # 새로운 리스트 객체 생성
# prog[0] = 'D'
# print("prog", prog)
# print("myprog", myprog)

# 타입 오류
# prog = ["C", "PYTHON", "JAVA", "GO"]
# myprog = prog + "HTML" # TypeError: can only concatenate list (not "str") to list
# =>
# prog = ["C", "PYTHON", "JAVA", "GO"]
# myprog = prog + ["HTML"] # 리스트 + 리스트 => 새로운 객체 생성
# print("myprog", myprog)

# 리스트 반복
# prog = ["C", "PYTHON", "JAVA"]
# data = [1, 2, 3]
# print(prog * 2) # 새로운 객체 생성, 2번 반복
# print(data * 3) # 새로운 객체 생성, 3번 반복

# 리스트 메소드들
# index
# print(dir([1, 2, 3])) # dir(객체) 메소드 리스트 출력
# prog = ["C", "PYTHON", "JAVA", "GO", "PYTHON"]
# print(prog.index('PYTHON')) # 리스트상 해당하는 객체의 첫번째 index
# print(prog.index('PHP')) # 리스트 내에 없으면 오류 발생
# print(prog.index('python')) # 대소문자 구분함

# append, extend, insert
# 뒤에 이어붙이기
# a = [1, 2, 3, 4]
# b = ["WEB", "OA", "Multi"]
# a.append(5)
# a.append("python")
# a.append([6, 7])
# a.append(b)
# print(a)

# extend - 리스트끼리 연산
a = [1, 2, 3, 4]
b = ["WEB", "OA", "Multi"]
a.extend(b) # a를 확장
print(a)
# a.extend(5) # list와 일반 객체 연산 불가

# insert(위치, 값) - 위치에 값을 추가
a = [1, 2, 3, 4]
a.insert(2, 5)
print(a)
# 'Excel'
b = ["WEB", "OA", "Multi", "RUBY"]
b.insert(2, "Excel")
print(b)
# 리스트 내 객체의 index번호 index(객체) 메소드
print(b.insert(b.index("OA") + 1, "Excel"))
print(b)

# 삭제
# del, pop, remove
b = ["WEB", "OA", "Multi", "RUBY"]
del b[1] # 버전2~
print(b)
del (b[1]) # 버전3~
print(b)

# pop()
a = ["WEB", "OA", "Multi", "RUBY"]
a.pop(2) # pop(index) 해당 index객체 삭제, Multi 삭제
a.pop() # pop() 제일 마지막 객체 제거, RUBY 삭제
a.pop() # OA 삭제
k = a.pop() # 해당 객체를 리턴해주고 삭제, 남은 WEB 삭제하면서 k에 담기
print(k)

# remove()
a = ["WEB", "OA", "Multi", "RUBY"]
a.remove("OA") # 해당 객체를 매개값으로 받음
print(a)
# a.remove("web") # ValueError: list.remove(x): x not in list, 대소문자 구분함

# count() # 리스트 내의 해당 객체의 갯수 출력
a = ["WEB", "OA", "Multi", "RUBY", "OA"]
print(a.count("OA"))
#
a = ["WEB", "OA", "Multi", "RUBY", "OA"]
print(a.count("python"))
if a.count("python"): # 파이썬에서 숫자 0은 False, 0 아닌 값 True
    a.remove("python")
    print(a)
else:
    print("삭제할 값이 없습니다.")

a = ["WEB", "OA", "Multi", "RUBY", "OA"]
print("OA" in a) # in은 객체 내에 해당 값이 있는지 여부 판단 True / False
print("python" in a)

a = ["WEB", "OA", "Multi", "RUBY", "OA"]
if "python" in a:
    a.remove("python")
    print(a)
else:
    print("없음")

# 정렬 sort() 메소드
a = [7, 9, 5, 1, 4, 8, 3, 2, 6]
a.sort() # 오름차순 정렬
print(a)
b = a.sort() # sort() 결과는 None 값을 리턴하지 않는 void 타입
print(b)
k = a.pop()
print(k)

# reverse
a = [7, 9, 5, 1, 4, 8, 3, 2, 6]
a.reverse()
print(a)

# 내림차순 정렬
# sort() 후 reverse()
a.sort()
a.reverse()
print(a)

# sorted()
a = [7, 9, 5, 1, 4, 8, 3, 2, 6]
b = sorted(a)
print(a)
print(b)
# 내림차순 정렬 sorted(리스트, reverse = True)
b = sorted(a, reverse = True)
print(b)

# len() 길이 함수
prog = ["C", "PYTHON", "JAVA", "GO"]
print(len(prog))
s = len(prog)
print(prog[s - 1]) # 리스트 길이(4) - 1 = 3(index 번호)
print(prog[-1]) # 역순법

# 리스트 내 반복문
data = ["cpu", "ram", "vga", "ssd", "dvd"]
for a in range(len(data)): # range(5) - 0 ~ 4
    print(data[a], end=" ")

a = ["WEB", "OA", "Multi", "RUBY"]
b = "\n".join(a)
print("\n".join(a))

data = [1, 2, 3, 4, 5]
print("-".join(map(str, data))) # [str(1), str(2), str(3), ..., str(5)]

data = [1, 2, 3, 4, 5]
print(data[0], type(data[0]))
a1, a2, a3, a4, a5 = map(str, data)
print(a1, type(a1))

# 리스트 내포 []
import random
data = []
for a in range(10):
    data.append(random.randint(10, 99))
print(data)

import random
data1 = [random.randint(10, 99) for a in range(10)]
print(data1)

data = [1, 2, 3, 4, 5]
data2 = []
for a in data:
    data2.append(a * a)
print(data2)

data2 = [a * a for a in data]
print(data2)

# 이차원 리스트
a = [[1, 2, 3], ["a", "b"], (10, 20, 30)]
print(a[0], a[0][1])
print(a[1][1])
print(a[2][1])

data = [[10101, "김창준", "rober@abc.com", 34],
        [10305, "심재호", "jhsi@abc.com", 23],
        [10515, "김은희", "ehkim@abc.com", 15],
        [10823, "박지원", "jhpark@abc.com", 25]]

# 이름, 이메일 출력
for a in range(len(data)): # 4
    print(data[a][1], data[a][2])

for a in data:
    print(a[1], a[2])