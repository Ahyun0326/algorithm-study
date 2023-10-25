import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

graph = [-1 for _ in range(f+1)]
queue = deque([s])
graph[s] = 0 # 방문 처리

dy = [u, -d]
while queue:

    y = queue.popleft()

    for i in range(2):
        ny = y + dy[i]

        if ny < 1 or ny > f:
            continue
        
        if (1 <= ny <= f) and graph[ny] == -1:
            queue.append(ny)
            graph[ny] = graph[y] + 1
    
    if y == g:
        break

if graph[g] == -1:
    print("use the stairs")
else:
    print(graph[g])
