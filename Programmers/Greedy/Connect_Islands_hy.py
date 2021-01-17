# programmers L3 : 단속카메라
# DATE : 2020.01.13
# Greedy 알고리즘

# Kruskal 알고리즘
# 최소 신장 트리(MST)
# 사이클을 이루지 않고, 최소 비용을 찾는 것
# 탐욕적인 방법을 이용하여 간선에 할당한 그래프의 모든 정점을 최소 비용으로 연결하는 최적의 해답 구함
# 노드를 모두 연결하는 최소 비용의 간선을 파악 -> 가중치 작은 간선부터 탐색하도록 정렬
# 이미 경로가 되어있는 곳에서 사이클이 만들어질 경우 그 간선은 선택하지 않음


#1. 그래프의 간선들을 오름차순으로 정렬
#2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선 선택
#3. 해당 간선을 현재의 집합에 추가(union-find 알고리즘
# ex) [{1}, {2}] ⇨ 간선(3, 4)추가  ⇨ [{1}, {2}, {3}, {4}]
# ⇨ 간선(2, 5) 추가 ⇨ [{1}, {2, 5}, {3}, {4}]
# ⇨ 간선(1, 2) 추가 ⇨ [{1, 2, 5}, {3}, {4}]


# Union-Find 란 Disjoint Set 을 표현할 때 사용하는 독특한 형태의 자료구조로,
#    공통 원소가 없는, 즉 "상호 배타적" 인 부분 집합 들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
#    입니다.
# 위의 상황을 표현하기 위해서는 초기화 과정과 다음과 같은 두 가지 연산을 지원해야 하기 때문에, Union-Find 자료구조 라고 부르게 되었다고 합니다.

# Union-Find 지원 연산
# 초기화 : N 개의 원소가 각각의 집합에 포함되어 있도록 초기화 합니다.
# Union (합치기) 연산 : 두 원소 a, b 가 주어질 때, 이들이 속한 두 집합을 하나로 합칩니다.
# Find (찾기) 연산 : 어떤 원소 a 가 주어질 때, 이 원소가 속한 집합을 반환합니다.
# https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 비용기준으로 오름차순 정렬
    bridge = []

    for i in range(n): # 섬의 개수만큼 집합 만들어줌
        bridge.append({i})

# 사이클이 형성되지 않도록 간선 선택
    # temp1, temp2 집합을 만듦
    for i in costs:
        temp1 = set()
        temp2 = set()
        # bridge for문 돌며 각 원소가 집합 안에 들어있는지 확인
        # 서로 다른 집합 안에 있으면 합침
        # 집합의 개수가 1개가 되면 반복문을 빠져나옴
        for j in bridge:
            if i[0] in j:
                temp1 = j
            if i[1] in j:
                temp2 = j
        if temp1 == temp2:
            continue
        else:
            bridge.remove(temp1)
            bridge.remove(temp2)
            bridge.append(temp1 | temp2)
            answer += i[2]
            if len(bridge) == 1:
                break

    return answer
print(solution(4, [[0, 1, 1], [0, 2, 3], [1, 2, 1], [1, 3, 1], [2, 3, 8]]))