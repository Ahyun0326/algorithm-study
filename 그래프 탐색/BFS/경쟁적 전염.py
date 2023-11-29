from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
s, x, y = map(int, input().split())

queue = []
# 바이러스가 낮은 것부터 큐에 삽입
for i in range(n):
    for j in range(n):
        # 바이러스가 존재하면
        if graph[i][j] != 0:
            # 바이러스, 위치, 시간
            queue.append((graph[i][j], i, j, 0))

# 바이러스가 작은 순으로 정렬 후 큐로 변경
queue.sort() 
queue = deque(queue)

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while queue:

    virus, a, b, time = queue.popleft()

    if time == s:
        break

    # 상,하,좌,우 탐색
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        # 범위를 벗어날 경우 continue
        if (ny < 0 or ny >= n) or (nx < 0 or nx >=n):
            continue

        # 바이러스가 존재하는 경우 continue
        if graph[nx][ny] > 0:
            continue

        # 바이러스 전염
        graph[nx][ny] = graph[a][b]
        queue.append((graph[nx][ny], nx, ny, time+1))
    
print(graph[x-1][y-1])
