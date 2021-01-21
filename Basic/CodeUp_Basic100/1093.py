# CodeUp 기초100제 : 1093
# [기초-1차원배열] 이상한 출석 번호 부르기1
# DATE : 2020.01.22

a =int (input())
b = input().split()
arr = []

for i in range(24):
    arr.append(0)
for i in range(a):
    arr[int(b[i])] += 1

for i in range(1, 24):
    print(arr[i], end=' ')
