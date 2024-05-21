import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):

    grid[y][x] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ny < 0 or ny > h-1 or nx < 0 or nx > w-1:
            continue
        if grid[ny][nx] == '.':
            continue

        dfs(nx, ny)

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                dfs(j, i)
                cnt += 1
    print(cnt)