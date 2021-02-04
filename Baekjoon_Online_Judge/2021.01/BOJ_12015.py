# Baekjoon Online Judge : 가장 긴 증가하는 부분 수열2
# DATE : 2020.02.01
# 이분탐색

# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n):
    start = 0
    end = len(answer) -1
    while start <= end: # A[i]보다 작거나 같은 수 중에 제일 큰 수 위치 찾음
        mid = (start + end) // 2
        if answer[mid] < a[i]:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(answer): # 위치가 배열보다 크다면 넣어줌
        answer.append(a[i])
    else : # 해당 위치의 숫자를 바꿔줌. 항상 작거나 같은 수 반환하기 때문에
        answer[start] = a[i]
print(len(answer))

# 정렬된 순서로 list유지하고자 할 때 bisect사용
# 구간의 인덱스를 얻을 때도 유용하게 사용 가능
# https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221389084876&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://soooprmx.com/archives/8722

# 정렬된 배열에서 특정한 원소를 찾아야할 때 매우 효과적
#  bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 반환
#  bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 반환

# bisect_left(arr, a) : arr 배열에서 a 값의 index를 반환
# a가 없으면 a보다 가장 가까운 큰 수의 index를 반환
# 모든 원소가 a보다 작으면 len(arr)을 반환
import sys
from bisect import bisect_left

def solution():
    answer = [] # 증가하는 수
    for a in A:
        # 비어있거나 top보다 클 경우 추가
        if not answer or a > answer[-1]:
            answer.append(a)
        else:   # a의 위치를 찾아 값 변경
            answer[bisect_left(answer, a)] = a

    print(len(answer))

# run test
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split(" ")))
solution()

# 테스트케이스
# 14
# 7 1 2 3 3 9 5 10 9 10 6 3 8 10
# correct = 7
#
# 5
# 10 1 2 3 11
# # 4
#
# 6
# 10 20 10 30 20 50
# # 4
#
# 10
# 10 4 1 3 5 1 2 3 4 6
# # 5