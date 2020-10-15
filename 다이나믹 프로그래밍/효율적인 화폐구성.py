n, m = map(int,input().split())
# N개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int, input())

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
