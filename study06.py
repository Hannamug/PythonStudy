# while문
login = True

# while login:
#     pw = input('password: ')
#     if pw == "test":
#         login = False
#         print("접속성공")
#     else:
#         print("비밀번호 오류!")

# id / pw 입력 "admin", "test" 둘 다 맞으면 접속성공
# id가 틀리면 "id오류", "비번오류"
# while문으로 작성
while login:
    id = input("ID: ")
    pw = input("PW: ")
    if id == "admin" and pw == "test":
        login = False
        print("접속성공")
    elif id != "admin" and pw == "test":
        print("id오류")
    elif id == "admin" and pw != "test":
        print("비번오류")
    else:
        print("접속실패")