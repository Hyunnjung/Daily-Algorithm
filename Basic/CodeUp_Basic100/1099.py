# CodeUp 기초100제 : 1099
# [기초-2차원배열] 설탕과자 뽑기
# DATE : 2020.01.22



# 시간초과
#
# a=[[0 for j in range(11)]for i in range(11)]
# for k in range(10):
#     x=list(map(int,(input().split())))
#     for l in range(10):
#         a[k+1][l+1]=x[l]
#
# m=2
# n=2
# while (a[m][n]!=2):
#     a[m][n]=9
#     if (a[m][n+1]==1 and a[m+1][n]==1) or (m==9 and n==9):
#         break
#     if a[m][n+1]==0:
#         n+=1
#     elif a[m][n+1]==1 and (a[m+1][n]==0 or a[m+1][n]==2):
#         m+=1
# a[m][n]=9
# for o in range(1,11):
#     for p in range(1, 11):
#         print(a[o][p],end=' ')
#     print('')

all = []
x = 1
y = 1
for i in range(10):
    a = list(map(int,input().split()))
    all.append(a)
while(True) :
    if all[x][y] == 2 : #먹이 발견했을때 break
        all[x][y] = 9
        break
    elif all[x+1][y] ==1 and all[x][y+1] ==1 :  #벽으로 가로 막혔을때 break
        all[x][y] = 9
        break
    all[x][y] = 9
    if all[x][y+1] == 1 :  #오른쪽이 벽이면 아래로 1칸
        x +=1
    elif all[x+1][y] == 1 :  # 아래쪽이 벽이면 오른쪽으로 1칸
        y += 1
    else : y+=1 # 주변에 벽이 없으면 오른쪽으로 1칸
for p in all :
    for o in p:
        print(o,end=" ")
    print()