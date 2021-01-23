# programmers L2 : 타겟넘버
# DATE : 2020.01.23
# DFS(깊이 우선 탐색)
# DFS : 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가 노드 방문한 수
#       다시 돌아가 다른 경로를 탐색하는 알고리즘



# 트리를 하나 만들어서 그 수를 뺀 수, 더한 수를 각각 노드로 만들어 붙여
# 최종 트리에서 target의 개수 세기
def solution(numbers, target):
    answer_tree = [0] # 첫 수부터 빼는 경우 있을 수 있어 0 담고 시작/ 이전 수에 대한 계산 결과 담음
    for num in numbers: # 매개변수로 받은 숫자 목록을 하나씩 꺼냄
        sub_tree = [] # 현재 숫자에 대한 결과를 담은 자식노드 하나씩 추가
        for tree_number in answer_tree:  # 노드 하나하나에 숫자를 더하고 빼서 자식 노드 생성
            sub_tree.append(tree_number+num)
            sub_tree.append(tree_number-num)
        answer_tree = sub_tree
    answer = answer_tree.count(target)
    return answer

print(solution([1,1,1,1,1], 3))


# 재귀함수로 푼 풀이
# def solution(numbers:list, target:int)->int:
#     if not numbers: # numbers 리스트 전부 소진
#         result = (1 if target == 0 else 0) # target 맞으면 1 return 아니면 0 리턴
#         return result
#     # numbers 리스트에 뭔가 남았을 경우 맨 뒤의 수 +,- 경우의 수 계산
#     return solution(numbers[:-1],target-numbers[-1]) + solution(numbers[:-1],target+numbers[-1])