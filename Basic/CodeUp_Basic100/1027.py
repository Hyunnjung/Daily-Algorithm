# CodeUp 기초100제 : 1027
# [기초-입출력] 연월일 입력받아 형식 바꿔 출력
# DATE : 2020.01.19


# 2014.07.12
# 15-07-2014
y,m,d = input().split()
print('%02d' %int(d), end='-')
print('%02d' %int(m), end='-')
print('%04d' %int(y))