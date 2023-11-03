import sys
from collections import deque


# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dh = [-1, 1, 0, 0, 0, 0]
dm = [0, 0, -1, 1, 0, 0]
dn = [0, 0, 0, 0, -1, 1]

# k, i, j => h, n, m
def bfs():

    while(queue):

        a, b, c = queue.popleft()
        
        # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
        for i in range(6):
            tmp_h = a + dh[i]
            tmp_m = c + dm[i]
            tmp_n = b + dn[i]

            if tmp_h<0 or tmp_h >=h or tmp_m<0 or tmp_m>=m or tmp_n<0 or tmp_n>=n:
                continue
            if graph[tmp_h][tmp_n][tmp_m] == 0 and visited[tmp_h][tmp_n][tmp_m] == False:
                visited[tmp_h][tmp_n][tmp_m] = True # 방문 처리
                graph[tmp_h][tmp_n][tmp_m] = graph[a][b][c] + 1 # 방문 날짜 증가
                queue.append([tmp_h, tmp_n, tmp_m])

m, n, h = map(int, sys.stdin.readline().split())

graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

queue = deque()
# 처음부터 익은 토마토들을 큐에 넣기
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1 and visited[k][i][j] == False:
                queue.append([k, i, j])
                visited[k][i][j] = True

bfs()

result = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
        
            result = max(result, graph[k][i][j])

print(result-1)
        

