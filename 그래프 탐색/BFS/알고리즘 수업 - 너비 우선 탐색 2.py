from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

num = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True)

queue = deque([r])
visited[r] = 1
cnt = 1

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1::]:
    print(i)
