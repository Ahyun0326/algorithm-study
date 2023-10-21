import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())    
    graph[x].append(y)
    graph[y].append(x)

queue = deque([b])
visited[b] = 0
cnt = 1

while queue:
    
    v = queue.popleft()
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = cnt
            queue.append(i)

    cnt += 1

if visited[a] == 0:
    print(-1)
else:    
    print(visited[a])
