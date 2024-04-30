# 디렉토리 파일관리 02
import os

path = r'c:\Temp'

for flist in os.scandir(path):
    if os.path.isfile(flist) and flist.name[-3:] == 'txt': # -3 을 한 이유는 파일 이름에서 확장자 부분만 따기 위해
        print(flist.name)

fname = 'hello.py'
file1 = fname.split('.')
print(file1, file1[0], file1[1])

for flist in os.scandir(path): # flist 에 path의 디렉토리 scan해서 넣고
    if os.path.isfile(flist): # flist 안의 file을 지정
        file1 = flist.name # file1 에 flist.name(== file)을 넣음
        f = file1.split('.') # file1에 들어간 flist.name을 . 기준으로 나누어 f에 넣음
        if f[1] == 'txt': # f에 넣은 것 중 인덱스 번호 1(== name)이 txt와 같다면
            # flist.name.split('.')[1] == 'txt'): # 'test1.txt'
            print(flist.name) # flist.name 파일들을 모두 출력

fname = 'python-3.9.7-amd64.exe'
file1 = fname.split('.')
print(file1, file1[:-1], file1[-1]) # [시작:끝], [:]
print(''.join(file1[:-1]), file1[-1])
print(''.join(file1[:-1]) + '.' + file1[-1])
id = 'hong'
pwd = '1234'
a = 'http://www.naver.com'
b = '/myapp/login?'
c = f'id={id}&pwd={pwd}'
print(''.join([a,b,c]))# 'http://www.naver.com/myapp/login?id=hong&pwd=1234'
print(''.join([a,b,c]).split('/'))

print('-------------------------------')
# splitext()
for flist in os.scandir(path):
    if os.path.isfile(flist):
        fn, fe = os.path.splitext(flist) # 확장자추출 .확장자(.txt)
        print(flist, fn, fe)
        if fe == '.py':
            print(flist.name)