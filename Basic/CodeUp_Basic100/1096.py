# CodeUp 기초100제 : 1096
# [기초-2차원배열] 바둑판에 흰 돌 놓기
# DATE : 2020.01.22


m = [[0]*19 for i in range(19)]

a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    m[b-1][c-1] = 1

for i in range(19):
    for j in range(19):
        print(m[i][j], end = ' ')
    print() # 리스트 안에 요소 출력


