import sys

location = sys.stdin.readline().strip()

move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] # 이동 가능한 경우의 수
start = [ord(location[0])-96, int(location[1])] # 나이트의 현재 위치 지정

cnt = 0
for i in range(len(move)):
    nx = start[0] + move[i][0]
    ny = start[1] + move[i][1]

    # 이동이 가능한 경우에만 cnt 증가
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)
