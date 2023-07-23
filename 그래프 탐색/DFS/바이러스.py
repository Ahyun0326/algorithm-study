computer = int(input())
connect = int(input())

# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  # print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 2차원 리스트의 맵 정보 입력 받기
graph = [[] for i in range(computer+1)]
visited = [False] * (computer + 1)
for i in range(connect):
  a,b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

#정의된 BFS 함수 호출
dfs(graph, 1, visited)
print(visited[2::].count(True))
