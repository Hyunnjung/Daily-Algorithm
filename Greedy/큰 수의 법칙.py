# 가장 큰 수, 두 번째로 큰 수만 저장하면 됨
# 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산 반복

# N,M,K 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수 정렬
data.sort()
first = data[N-1] # 제일 큰 수
second = data[N-2] # 두 번째 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M - count) * second # 두 번째로 큰 수 더하기

print(result)
