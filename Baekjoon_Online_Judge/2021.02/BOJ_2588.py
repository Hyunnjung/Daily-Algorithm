# Baekjoon Online Judge : 곱셈
# DATE : 2020.02.11

a = int(input())
b = input()

for i in range(3):
    result = a*int(b[2-i])
    print(result)
print(a*int(b))