import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
tmp = [[0]*m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 바이러스가 퍼질 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if tmp[nx][ny] == 0: # 빈 칸이면
                tmp[nx][ny] = 2 # 바이러스 전파
                virus(nx,ny)

result = 0
# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(cnt):

    global result
    # 울타리가 3개 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최댓값 계산
        score = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 0:
                    score += 1

        result = max(result, score)
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1

dfs(0)
print(result)
