import sys
sys.setrecursionlimit(10**6)

move = [-1, 1]
def dfsY(x, y):

    visited[y][x] = True

    for i in range(2):
        ny = y + move[i]

        if 0 <= ny < n and graph[ny][x] == '|': 
            if not visited[ny][x]:
                dfsY(x, ny)

def dfsX(x, y):

    visited[y][x] = True

    for i in range(2):
        nx = x + move[i]

        if 0 <= nx < m and graph[y][nx] == '-':
            if not visited[y][nx]:
                dfsX(nx, y)


n, m = map(int, input().split())
graph = []
visited =[[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    floor = list(input())
    graph.append(floor)

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == '-':
            dfsX(j, i)
            cnt += 1
        elif not visited[i][j] and graph[i][j] == '|':
            dfsY(j, i)
            cnt += 1
print(cnt)
