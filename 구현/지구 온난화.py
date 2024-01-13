import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for i in range(r):
    line = list(input().strip())
    graph.append(line)

# 상,하,좌,우 연산 정의
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 50년 후 잠기는 위치들을 저장하는 리스트
pos = []

# 그래프 탐색
for i in range(r):
    for j in range(c):
        
        cnt = 0
        # 섬일 경우 인접한 부분 탐색
        if graph[i][j] == 'X':
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]

                # 인접한 곳이 범위를 벗어날 경우 바다이므로 cnt 증가
                if (nx < 0 or nx > c-1) or (ny < 0 or ny > r-1):
                    cnt += 1
                # 인접한 곳이 바다이고 인접한 부분이 50년 뒤 잠기지 않는다면 cnt 증가
                elif (graph[ny][nx] == '.') and (ny, nx) not in pos:
                    cnt += 1
            
        # 섬과 인접한 바다가 3개 이상이면
        if cnt >= 3:
            # 현재 위치를 저장하고 바다로 바꾸기
            graph[i][j] = '.'
            pos.append((i,j))

left = 10
right = 0
up = 10
down = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
        # 가장 왼쪽에 있는 값
            if j < left:
                left = j
        # 가장 오른쪽에 있는 값
            if j > right:
                right = j
        # 가장 위쪽에 있는 값
            if i < up:
                up = i
        # 가장 아래쪽에 있는 값
            if i > down:
                down = i

for i in range(up, down+1):
    for j in range(left, right+1):
        print(graph[i][j], end= '')
    print()
