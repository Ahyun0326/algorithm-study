import sys
input = sys.stdin.readline

# 보드의 크기 N 입력 받기
n = int(input())
# 사과의 개수 k 입력 받기
k = int(input())
# 사과의 위치를 담은 리스트
apple = [list(map(int, input().split())) for _ in range(k)]
# 뱀의 방향 변환 횟수 L 입력 받기
l = int(input())
# 뱀의 방향 변환 정보를 담은 리스트
snake = [list(input().split()) for _ in range(l)]

# 왼쪽, 또는 오른쪽으로 회전하는 함수
def turn(x, d):

    if x == 'D':
        if d == 3:
            d = 0
        else:
            d += 1 
    else:
        if d == 0:
            d = 3
        else:
            d -= 1

    return d

# 게임의 시간을 계산하기 위한 cnt
cnt = 0

# 뱀의 현재 위치 저장할 리스트
pos = [[0,0]]

# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 처음 바라보는 방향은 오른쪽
d = 0

# 그래프의 크기만큼 반복
for i in range(n):
    for j in range(n):

        # 방향 전환 정보에 따라 방향 전환
        if len(snake) != 0 and int(snake[0][0]) == cnt:
            d = turn(snake[0][1], d)
            snake.pop(0)

        # 바라보는 방향으로 이동하기 위한 연산
        nx = pos[-1][1] + dx[d]
        ny = pos[-1][0] + dy[d]

        # 시간 증가
        cnt += 1

        # 자기 자신에게 부딪혔거나 벽에 부딪혔다면 종료
        if [ny, nx] in pos or (ny < 0 or ny > n-1) or (nx < 0 or nx > n-1):
            print(cnt)
            exit(0)
          
        # 사과가 있다면
        if len(apple) != 0 and ([ny+1, nx+1] in apple):

            apple.remove([ny+1, nx+1])
              
            # 뱀위 길이를 늘려 위치 추가
            pos.append([ny, nx])
    
        # 사과가 없다면
        else:
                
            # 길이를 늘리지 않고 현재 위치만 추가
            pos.append([ny, nx])
            
            # 이동했으므로 이전 위치 제거
            pos.pop(0)
