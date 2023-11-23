import sys
sys.setrecursionlimit(10**6)

# 연산자 정의
# 상,하,좌,우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(x, y):

    # 방문 처리
    visited[y][x] = True

    # 상,하,좌,우 탐색
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 얼음 틀 범위를 넘어가지 않고
        if 0<=ny<n and 0<=nx<m:
            # 구멍이 뚫려있고, 아직 방문되지 않은 곳이면
            if visited[ny][nx] == False and graph[ny][nx] == 0:
                dfs(nx, ny) #dfs 수행 


n, m = map(int, input().split())

graph = []
visited = [[False for _ in range(m)] for _ in range(n)] 
for i in range(n):
    a = list(map(int,input()))
    graph.append(a)

cnt = 0
for i in range(n):
    for j in range(m):
        # 아직 방문되지 않은 정점이고 구멍이 뚫려 있는 부분이면
        if not visited[i][j] and graph[i][j] == 0:
            # dfs 수행
            dfs(j, i)
            cnt +=1

print(cnt)
