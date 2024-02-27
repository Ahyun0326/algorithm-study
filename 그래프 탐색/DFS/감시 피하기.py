import sys
input = sys.stdin.readline
    
n = int(input())
graph = [input().split() for _ in range(n)]

teacher = 0
for i in range(n):
    teacher += graph[i].count('T')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs 함수
def check(x, y):

    # 상, 하, 좌, 우 직선 방향으로 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':

            # 만약 탐색 도중 학생이 발견되었다면
            if graph[nx][ny] == 'S':
                # 감시 성공
                return True
            
            # 발견되지 않았다면 그 다음 위치 탐색
            else:
                nx += dx[i]
                ny += dy[i]

    # 감시 실패
    return False 

def solution(cnt):

    global result

    # 장애물이 3개가 설치되었고    
    if cnt == 3:
        teacher_cnt = 0
        for i in range(n):
            for j in range(n):
                # 선생님이 있다면 check 함수 수행
                if graph[i][j] == 'T':
                    # 모든 선생님이 감시가 불가능하면
                    if not check(i,j):
                        teacher_cnt += 1
        
        # 모든 선생이 감시가 불가능하면
        if teacher_cnt == teacher:
            result = True
        return 

    # 모든 경우에 대해 장애물 설치해가며 DFS 수행
    for i in range(n):
        for j in range(n):
            # 만약 복도에 아무것도 존재하지 않는다면
            if graph[i][j] == 'X':
                # 장애물 설치
                graph[i][j] = 'O'
                cnt += 1
                solution(cnt)
                graph[i][j] = 'X'
                cnt -= 1

result = False
solution(0)

if result:
    print("YES")
else:
    print("NO")
