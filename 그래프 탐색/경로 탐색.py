import sys
INF = sys.maxsize

n = int(sys.stdin.readline().strip())
graph = [0 for _ in range(n)]

for i in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    graph[i] = s

# 플로이드 알고리즘
for k in range(n): # 거치는 점
    for j in range(n): # 시작점
        for i in range(n): # 끝점
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):            
    for j in range(n):
        print(graph[i][j], end = ' ')
    print()

