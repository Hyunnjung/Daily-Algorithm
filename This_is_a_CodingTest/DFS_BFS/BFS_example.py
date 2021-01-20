# BFS(Breadth First Search) 너비 우선 탐색
#
# - O(N) (DFS보다 수행시간 좋은 편)
# - 가까운 노드부터 탐색하는 알고리즘
# - 선입선출 구조인 큐 자료구조 이용
#
# * 동작 방식
#   1. 탐색 시작 노드를 큐에 삽입하고 방문 처리 함
#   2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
#   3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
# deque라이브러리 사용하는 것이 좋음



from _collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue)구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    ...
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 BFS함수 호출
bfs(graph, 1, visited)