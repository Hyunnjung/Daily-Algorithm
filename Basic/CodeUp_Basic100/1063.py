# CodeUp 기초100제 : 1063
# [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
# DATE : 2020.01.20

a, b = input().split()
x= int(a)
y= int(b)
print(x if x>y else y)