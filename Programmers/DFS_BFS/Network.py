# programmers L3 : 네트워크
# DATE : 2020.01.23
# 백준 2606(바이러스)와 문제 비슷
# BFS


# BFS 구현
# 1. 탐색을 위한 큐, 방문한 노드를 체크해 둘 리스트 생성
# 2. 탐색을 시작할 노드를 큐에 넣기 (탐색 시작 노드의 방문 표시 해두기)
# 3. 큐가 빌 때까지 반복문 수행
#     1.큐의 앞에서부터 노드를 하나씩 꺼내기
#     2.꺼낸 노드에 인접한 노드들을 방문하는 반복문 수행
#         -방문한 노드가 이전에 방문한 적이 없다면 큐에 넣기
#         -방문한 노드는 체크해두기

def solution(n, computers):
    answer = 0  # 네트워크의 개수 저장할 곳
    bfs = []  # 탐색을 위한 큐
    visited = [0] * n  # 방문한 노드를 체크해 둘 리스트

    while 0 in visited: # vistied 리스트의 모든 값에 방문 표시가 되어있을 때까지 반복
        x = visited.index(0)
        bfs.append(x) # 큐에 첫 노드 추가
        visited[x] = 1  # 첫 노드 방문표시

        while bfs: # 큐의 값이 존재하면 반복문 수행
            node = bfs.pop(0)  # 큐의 앞에서부터 노드 꺼냄
            visited[node] = 1
            for i in range(n): # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
                if visited[i] == 0 and computers[node][i] == 1:  # 인접 노드이고, 방문된 적 없는 경우
                    bfs.append(i) # 큐에 추가
                    visited[i] = 1 # 방문했음 표시
        answer += 1 # 한 네트워크의 탐색을 마치면 개수 추가
    return answer

