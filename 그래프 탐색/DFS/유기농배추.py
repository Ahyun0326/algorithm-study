import sys
sys.setrecursionlimit(10**6)

def dfs(x, y): # 상하좌우 탐색
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())    # 가로, 세로, 
    graph = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):  # 배추가 있는 곳 1로 설정
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                count += 1
    print(count)
