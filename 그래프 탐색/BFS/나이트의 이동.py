import sys
from collections import deque

t = int(sys.stdin.readline())
move = [[-2,-1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for i in range(t):
    l = int(sys.stdin.readline())
    start_a, start_b = map(int, sys.stdin.readline().split())
    end_a, end_b = map(int, sys.stdin.readline().split())

    visited = [[-1 for _ in range(l)] for _ in range(l)]
    queue = deque([[start_a, start_b]])    
    visited[start_a][start_b] = 0 # 방문 처리

    result = 0
    while queue:
        
        y, x = queue.popleft()
        
        for i in range(8):
            ny = y + move[i][0] 
            nx = x + move[i][1]
        
            if (0<=ny<l and 0<=nx<l) and visited[ny][nx] == -1:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

        if y == end_a and x == end_b:
            break
        
    print(visited[end_a][end_b])       
