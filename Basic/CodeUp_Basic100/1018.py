# CodeUp 기초100제 : 1018
# [기초-입출력] 시간 입력받아 그대로 출력하기
# DATE : 2020.01.19

h,m = input().split(':')
print(int(h), int(m), sep=':')

# sep(separation) : 구분자
# >>> print('S','E','P', sep = '@'
# S@E@P