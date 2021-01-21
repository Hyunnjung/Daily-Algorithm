# CodeUp 기초100제 : 1097
# [기초-2차원배열] 바둑알 십자 뒤집기
# DATE : 2020.01.22

#0으로 채워진 바둑판 리스트 생성
a=[[0 for j in range(20)] for i in range(20)]


for k in range(19):
    x=list(map(int,(input().split())))
    for l in range(19):
        a[k+1][l+1]=x[l]
# 십자뒤집기 횟수, 좌표 입력 후 횟수만큼 뒤집기 반복
n=int(input())
for v in range(n):
    v1,v2=map(int,(input().split()))
    for m in range(1,20):
        if a[v1][m]==0:
            a[v1][m]=1
        else:
            a[v1][m]=0
        if a[m][v2]==0:
            a[m][v2]=1
        else:
            a[m][v2]=0
 # 뒤집기 완료된 바둑판 출력
for o in range(1,20):
    for p in range(1,20):
        print(a[o][p],end=' ')
    print('')