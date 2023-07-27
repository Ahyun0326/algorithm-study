import sys

sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().split())

def dfs(graph, visited, r, cnt):
    visited[r] = cnt # 시작 정점을 방문 처리
    # 인접 정점 탐색
    for i in graph[r]:
        if visited[i] == -1: # 아직 방문되지 않은 정점이라면
            dfs(graph, visited, i, cnt+1)

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]  # 방문되지 않는 노드의 깊이는 -1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순으로 graph 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)

cnt = 0
dfs(graph, visited, r, cnt)

for i in visited[1::]:
    print(i)
