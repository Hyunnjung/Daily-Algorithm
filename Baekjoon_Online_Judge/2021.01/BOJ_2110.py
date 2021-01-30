# Baekjoon Online Judge : 공유기 설치
# DATE : 2020.01.30
# 이분탐색

import sys
N, C = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

start = 1 # 최소 간격
end = house[-1] - house[0] #최대 간격
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1 # 공유기의 개수(처음 설치하고 시작)
    cur = house[0]
    for i in range(1, N):
        if house[i] - cur >= mid:
            count += 1
            cur = house[i]
    # 설치 가능한 집의 개수 >= C : 공유기 사이의 거리 늘릴 수 있음
    # start 를 mid + 1로 바꿈(이분)
    if count >= C:
        start = mid + 1
        answer = mid
    else: # 설치 가능한 집의 개수 < C : 공유기 사이의 거리 줄여야 함
        end = mid - 1

print(answer)


