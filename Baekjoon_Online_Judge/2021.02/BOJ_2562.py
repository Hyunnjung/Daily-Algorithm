# Baekjoon Online Judge : 최댓값
# DATE : 2020.02.11

a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)