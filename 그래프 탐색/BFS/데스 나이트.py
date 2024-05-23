import sys
input = sys.stdin.readline
from collections import deque

# 연산자 정의
move = [[-2,-1], [-2,1], [0,-2], [0,2], [2,-1], [2,1]]
def bfs():
    while queue:
        x, y = queue.popleft()
        
        if x==r2 and y==c2:
            return
        
        for i in move:
            nx = x+i[0]
            ny = y+i[1]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            if board[nx][ny] != 0:
                continue

            queue.append([nx,ny])
            board[nx][ny] = board[x][y] + 1

n = int(input())
r1,c1,r2,c2 = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
queue = deque()
queue.append([r1, c1])

bfs()
if board[r2][c2] == 0:
    print(-1)
else:
    print(board[r2][c2])
