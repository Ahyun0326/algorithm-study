import sys
sys.setrecursionlimit(10**9)

    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
    
def dfs(x, y):

    global house_cnt
    visited[y][x] = 1
    house_cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
            if visited[ny][nx] == -1:
                dfs(nx, ny)
    
    return house_cnt

n = int(sys.stdin.readline())
graph = [sys.stdin.readline().strip() for _ in range(n)]
visited = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(len(graph)):
    graph[i] = list(map(int, graph[i]))

house_list = []
for i in range(n):
    for j in range(n):
        if visited[j][i] == -1 and graph[j][i] == 1:            
            house_cnt = 0
            house_cnt = dfs(i, j)
            house_list.append(house_cnt)

print(len(house_list))
house_list.sort()
for i in house_list:
    print(i)
