import sys
sys.setrecursionlimit(10**9)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, sys.stdin.readline().split())
campus = []
for i in range(n):
    info = list(sys.stdin.readline().strip())
    campus.append(info)

def dfs(x, y):
    global cnt

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            continue
        if campus[ny][nx] == 'X':
            continue
        
        if campus[ny][nx] == 'O':
            campus[ny][nx] = 'X'
            dfs(nx, ny)
        elif campus[ny][nx] == 'P':
            campus[ny][nx] = 'X'
            cnt += 1
            dfs(nx, ny)

cnt = 0
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            dfs(j, i)

if cnt == 0:
    print('TT')
else:
    print(cnt)