# Quiz 02
# 입력한 시간의 형식을 변경하시오.
# 입력: 시간을 [시:분:초] 형식으로 입력한다.
#      0 <= 시 < 24, 0 <= 분 < 60, 0 <= 초 < 60
# 출력: 24시간 형식의 시간을 [오전 0시 0분 0초]로 출력한다.
# h, m, s = map(int, input().split(':'))
#
# ampm = '오전'
# if h >= 12:
#     ampm = '오후'
#
# if h > 12:
#     h -= 12
#
# print(f'{ampm} {h}시 {m}분 {s}초')

# Quiz 04
# N명의 심사위원의 점수의 합계를 출력하시오. 단, 가장 높은 점수와 낮은 점수
# 를 제외한 점수는 제외하시오. 가장 높은 점수가 중복될 경우 값 하나만 삭제
# 입력: 심사위원의 수만큼 점수를 한 칸 단위로 입력한다.
# 출력: 최댓값과 최솟값을 제외한 점수의 합계를 출력한다.
# score = list(map(int, input().split(' ')))
# score.remove(max(score))
# score.remove(min(score))
# print(sum(score))

# Quiz 05
# 연속해서 정답을 맞출 경우 배점이 달라지는 시험이 있다.
# 입력: n개의 채점결과를 'O', 'X'로 연속해서 입력한다.
# 출력: 'O'가 1개만 있을 경우 1점, 연속해서 있을 떄는 연속한 수가 점수이다.
# 예) OXX : 1점(1+0+0), OOX : 3점(1+2+0), OXOXO : 3점(1+0+1+0+1),
#    XOOOX : 6점(0+1+2+3+0), OOXOO : 6점(1+2+0+1+2)
# sel = list(input())
# score = 0
# result = 0
#
# for a in range(len(sel)):
#     if sel[a] == 'O':
#         score += 1
#         result += score
#     else:
#         score = 0
#
# print(result, "점")

# Quiz 06
# 입력한 문장에서 사용하지 않은 알파벳 글자를 출력하시오.
# 입력: 한 문장을 입력한다.
# 출력: a부터 z까지 사용하지 않은 글자를 출력한다.
#      단, 소문자만 입력한다.
# from string import ascii_lowercase
# alphabet = list(ascii_lowercase)
# sent = input()
#
# for a in range(len(sent)):
#     if sent[a] in alphabet:
#         alphabet.remove(sent[a])
#
# print(''.join(alphabet))

# Quiz 07
# 정수를 입력하면 각 자릿수의 숫자의 합을 출력하시오.
# num = list(map(int, input()))
# result = 0
# for a in range(len(num)):
#     result += num[a]
#
# print(result)

# Quiz 08
# 입력한 n개의 단어를 출현 빈도수가 높은 단어 3개를 출력하시오.
# 입력: 단어를 한 칸 단위로 n개 입력한다.
# 출력: 가장 많이 등장한 단어부터 단어와 출현 빈도수를 3개 출력한다.
# sent = list(input().split(" "))
# dir = {}
#
# for a in sent:
#     if a in dir.keys():
#         dir[a] += 1
#     else:
#         dir[a] = 1
#
# dir_sort = sorted(dir.items(), reverse = True, key = lambda x:x[1])
# for a in range(3):
#     print(dir_sort[a][0], ":", dir_sort[a][1])