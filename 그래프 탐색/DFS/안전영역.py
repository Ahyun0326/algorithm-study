import sys
sys.setrecursionlimit(100000)

def dfs(x, y, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and h < graph[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny]= True
                dfs(nx, ny, h)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_h=0
for i in range(n):
    if max_h < max(graph[i]):
        max_h = max(graph[i])

answer = 1
for h in range(max_h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and graph[x][y] > h:
                cnt += 1
                visited[x][y] = True
                dfs(x,y,h)
    answer = max(answer, cnt)

print(answer)
