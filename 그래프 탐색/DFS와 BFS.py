import sys
from collections import deque

def dfs(start):

    dfs_visited[start] = True # 방문 처리
    print(start, end= ' ') # 방문정점 출력

    for i in graph[start]:
        # 아직 방문되지 않았다면
        if dfs_visited[i] == False:
            dfs(i) # 해당 정점 탐색


def bfs():
    
    while queue:

        a = queue.popleft()
        bfs_visited[a] = True
        print(a, end = ' ')

        for i in graph[a]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                queue.append(i)


# 정점 개수, 간선의 수, 시작점
n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
graph[0].append(0)
dfs_visited = [False for _ in range(n+1)]
bfs_visited = [False for _ in range(n+1)]
queue = deque([v])

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(v)
print()
bfs()
