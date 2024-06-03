import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    
    while queue:
        x = queue.popleft()
        if x == m:
            return pos[x]
        
        for i in range(8):
          if i == 6 or i == 7:
            nx = x * move[i]
          else:
            nx = x + move[i]  

          if nx < 0 or nx > 100000:
                continue
          
          if pos[nx] != 0:
                continue
          queue.append(nx)
          pos[nx] = pos[x] + 1

# 스카이 콩콩의 힘 A와 B, 동규, 주미의 현재 위치
a, b, n, m = map(int, input().split())
pos = [0 for _ in range(100001)]
                                                                                                               
# 현 위치에서 +-1칸
# 현 위치에서 +-A, +-B칸
# 현 위치의 A, B배의 칸
move = [-1, 1, -a, a, -b, b, a, b]
queue = deque()
queue.append(n)
print(bfs())