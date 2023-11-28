from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

start = x
queue=deque([x])
visited[start] = 0

while queue:

    v = queue.popleft()
    
    # 연결된 정점 탐색
    for i in graph[v]:
        # 방문되지 않은 정점이면
        if visited[i] == -1:
            # 큐에 추가
            queue.append(i)
            # 방문 횟수를 증가
            visited[i] = visited[v] + 1

if visited.count(k) == 0:
    print(-1)
    exit(0)

for i in range(1, len(visited)):
    if visited[i] == k:
        print(i)


