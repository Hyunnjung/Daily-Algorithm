# programmers L3 : 단어 변환
# DATE : 2020.01.24
# DFS/BFS

# 한 글자만 다른 단어 = 연결되어 있는 노드

def dfs(begin, target, words):
    visited = []
    stack = [begin]

    while stack:
        n = stack.pop()
        if n == target:
            break
        if n not in visited:
            visited.append(n)
        print(visited)
        # 하나만 다른 단어를 찾기
        for word in words:
            # 한 개의 알파벳만 다른 경우
            if word not in visited and len([i for i in range(len(word)) if n[i] != word[i]]) == 1:
                stack.append(word) # 스택에 추가

    return len(visited)

def solution(begin, target, words):
    if target not in words: # words에 target에 없을 경우, 0 반환
        return 0

    else:
        return dfs(begin, target, words)
