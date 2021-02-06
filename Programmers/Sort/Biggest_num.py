# programmers L2 : 가장 큰 수
# DATE : 2020.02.06
# 정렬


def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers의 원소는 0이상, 1000이하라는 조건 통해
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# [6,10,2] -> [666, 101010, 222] -> [666, 222, 101010]
# 문자열의 비교연산의 경우 첫번째 인덱스인 6,1,2 를 아스키로 바꿔서 비교