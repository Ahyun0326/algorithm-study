import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0 

# 각 간선에 대한 정보를 입력 받아, 그 정보를 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 수행된 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):      
        # 갈 수 없는 경우 0 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        #갈 수 있는 경우 최단 경로 출력
        else:
            print(graph[i][j], end=' ')
    print()
