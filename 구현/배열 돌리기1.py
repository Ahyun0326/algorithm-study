import sys

n, m, r = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 돌려야 할 사각형의 개수 계산
cnt = min(n, m)//2

for k in range(r):
    # 사각형의 개수만큼 반복해서 배열 돌리기
    for i in range(cnt):

        # 이동할 횟수 계산
        x = m-i-1         # 가로
        y = n-i-1         # 세로
        tmp = array[i][x] # 맨 앞에 있는 값 저장

        # 왼쪽으로 이동
        for j in range(x-1, i-1, -1):
            prev = array[i][j]
            array[i][j] = tmp
            tmp = prev
            
        # 아래로 이동
        for j in range(i+1, y+1):
            prev = array[j][i]
            array[j][i] = tmp
            tmp = prev
            
        # 오른쪽으로 이동
        for j in range(i+1, x+1):
            prev = array[y][j]
            array[y][j] = tmp
            tmp = prev

        # 위로 이동
        for j in range(y-1, i-1, -1):
            prev = array[j][x]
            array[j][x] = tmp
            tmp = prev

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()
