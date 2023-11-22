from collections import deque

def bfs(graph, start):
    num = [0 for _ in range(n+1)]
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        # 인접 정점 탐색
        for i in graph[a]:
            # 시작 정점이 아닌 인접 정점이면
            if i not in visited:
                num[i] = num[a] + 1 # 카운트 증가
                visited.append(i)  
                queue.append(i) # 큐에 추가

    return(sum(num))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)

