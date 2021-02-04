# programmers L1 : k번째 수
# DATE : 2020.02.04
# 정렬

def solution(array, commands):
    answer = []
    for command in commands: #command마다 리스트 자르고 정렬
        array2 = array[command[0]-1:command[1]]
        array2.sort()
        answer.append(array2[command[2]-1])
    return answer