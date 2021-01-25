# programmers L3 : 여행 경로
# DATE : 2020.01.24
# DFS

# 가야하는 다음 경로 : stack.top을 시작점으로 하는 끝점들을 역순으로 저장하는 리스트의 가장 마지막 원소
def solution(tickets):
    routes = {} # 딕셔너리 구성
    for t in tickets: # 출발지:도착지 dic만듦
        if t[0] not in routes.keys():
            routes[t[0]] = [t[1]]
        else:
            routes[t[0]] = [t[1]]
    for r in routes.keys(): # 딕셔너리 돌면서 항공권 리스트 역순 정렬/ pop()대비해 알파벳순서대로 뽑히도록
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack: # 스택이 빌때까지 반복
        top = stack[-1] # 스택에서 가장 위 저장된 데이터 top꺼내옴
        if top in routes and routes[top]: # top이 그래프에 없거나 top을 시작점으로 하는 티켓이 없는 경우 스택에서 꺼내와 path에 저장
            stack.append(routes[top].pop())
        else: # top을 시작점으로 하는 끝점 중 가장 마지막 지점 꺼내와 스택에 저장
            path.append(stack.pop())

    return path[::-1] # path 거꾸로 돌림(스택은 선입후출이기때문)