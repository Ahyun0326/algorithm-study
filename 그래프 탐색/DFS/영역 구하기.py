import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):

    global cnt
    triangle[y][x] = 1
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ny < 0 or ny > m-1 or nx < 0 or nx > n-1:
            continue
        if triangle[ny][nx] == 1:
            continue

        dfs(nx, ny)

m,n,k = map(int, input().split())
triangle = [[0 for _ in range(n)] for _ in range(m)]
array = []
for i in range(k):
    array.append(list(map(int, input().split())))

    for a in array:
        xl, yl, xr, yr = a[0], a[1], a[2], a[3]
        yl = m-yl
        yr = m-yr
        for h in range(yr, yl):
            triangle[h][xl:xr] = [1] * (xr-xl)

result = []
for i in range(m):
    for j in range(n):
        if triangle[i][j] == 0:
            cnt = 0
            dfs(j, i)
            result.append(cnt)
            
result.sort()
print(len(result))
print(*result)
 