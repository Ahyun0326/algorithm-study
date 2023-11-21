n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0 ,1, 0, -1]
turn_cnt = 0
result = 0
while(True):

    # 현재 칸이 청소되지 않은 경우
    if room[r][c] == 0:
        room[r][c] = -1
        result += 1
        
    d -= 1
    if d == -1:
        d = 3

    ny = r + dy[d]
    nx = c + dx[d] 
    turn_cnt += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if room[ny][nx] == 0:
        # 한 칸 전진
        r = ny
        c = nx
        turn_cnt = 0
        continue

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    elif turn_cnt == 4:
        # 바라보는 상태를 유지하고 뒤로 후진
        ny = r - dy[d]
        nx = c - dx[d]  

        if room[ny][nx] == 1:
            break
  
        r = ny
        c = nx
        turn_cnt = 0


print(result)
