import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())    
    graph[x].append(y)
    graph[y].append(x)

queue = deque([a])
visited[a] = 1
cnt = 1
while queue:
    v = queue.popleft()
    
    if v == b:
        break

    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + cnt
            queue.append(i)

if visited[b] != -1:
    if visited[a] > visited[b]:
        print(visited[a] - visited[b])
    elif visited[a] < visited[b]:
        print(visited[b] - visited[a])
elif visited[b] == -1:
    print(visited[b])
