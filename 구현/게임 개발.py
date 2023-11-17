import sys

n, m = map(int, sys.stdin.readline().split())
a, b, d = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0 ,-1]

visited[a][b] = True
cnt = 0
turn_time = 0
while True:

    d -= 1 # 반시계 방향으로 회전
    if d == -1:
        d = 3

    nx = a + dx[d]
    ny = b + dy[d]

    # 가보지 않은 칸이면 회전한 방향으로 전진
    if graph[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True # 방문 처리
        a = nx
        b = ny
        cnt += 1
        turn_time = 0
        continue 

    # 가보지 않은 칸이 없다면 왼쪽으로 회전만
    else:
        turn_time += 1

    # 네 방향 모두 이미 가본 칸이거나 바다라면
    if turn_time == 4:
        nx = a - dx[d]
        ny = b - dy[d]

        # 바라보는 방향 유지한 채로 뒤로 가기
        if graph[nx][ny] == 0:
            a = nx
            b = ny

        # 뒤로 갈 수 없는 경우 움직임 중단
        else:
            break

        turn_time = 0

print(cnt)
