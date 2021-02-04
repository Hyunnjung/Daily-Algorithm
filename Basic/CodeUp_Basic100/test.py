
n = int(input())
num = list(map(int, input().split()))

for i in range(24):
    num.append(0)
for i in range(n) : 
    num[b[i]]+=1
for i in range(1, 24) :
    print(num[i], end=' ')

