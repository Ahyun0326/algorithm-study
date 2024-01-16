import sys
input = sys.stdin.readline

n = int(input())
# 도시간에 이동하는데 드는 비용 입력 받기
graph = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)

def dfs(start, next, value, visited):
    global res

    if len(visited) == n:
        if graph[next][start] != 0:
            res = min(res, value + graph[next][start])
        return
    
    for i in range(n):
        if graph[next][i] != 0 and i not in visited and i != start:
            visited.append(i)
            dfs(start, i, value + graph[next][i], visited)
            visited.pop()

for i in range(n):
    dfs(i, i, 0, [i])

print(res)
