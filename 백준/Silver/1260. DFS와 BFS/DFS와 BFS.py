N, M, V = map(int, input().split())         # N: 정점의 개수, M: 간선의 개수, V: 시작 정점
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())        # 이어져있는 정점 입력
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()


## DFS
visited = [False] * (N + 1)
def dfs(start):
    visited[start] = True                   # 정점 방문 표시
    print(start, end=" ")                   # 시작 정점 출력 : 1

    for i in graph[start]:                  # 정점 1의 이웃
        if not visited[i]:
            dfs(i)

dfs(V)
print()


## BFS
visited = [False] * (N + 1)
from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:                        # queue가 비어있을때까지 계속 
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(V)