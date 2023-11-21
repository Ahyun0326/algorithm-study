n, m = map(int, input().split())

def dfs(v):

    # 방문 처리
    visited[v] = True

    #인접 정점 탐색
    for i in graph[v]:
        # 아직 방문되지 않은 정점이면
        if not visited[i]:
            dfs(i) # dfs

graph = [[] for _ in range(n+1)]
graph[0].append(0)
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
# 모든 정점에 대해 dfs 수행
for v in range(1,n+1):
    if not visited[v]:
        dfs(v)
        cnt +=1

print(cnt)
