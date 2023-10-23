import sys
from collections import deque

n, m = map(int,(sys.stdin.readline().split()))

graph = [[] for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a = list(map(int, sys.stdin.readline().strip()))
    graph[i] = a

# print(graph)

queue = deque([[0,0]])
visited[0][0] = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:

    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 1:
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    

print(visited[n-1][m-1])
