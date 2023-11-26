from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a = list(map(int, input()))
    graph.append(a)

# 시작 지점을 큐에 넣기
queue = deque([(0,0)])

# 상하좌우 연산
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 첫 시작 정점 1로 설정
visited[0][0] = 1

# 큐가 빌 때까지 반복
while queue:

    # 큐에서 정점 꺼내기
    y, x = queue.popleft()

    # 인접 정점 모두 탐색
    for i in range(4):
        
        ny = y + dy[i]
        nx = x + dx[i]

        # 미로의 범위를 벗어나지 않고, 괴물이 없다면 (1이라면)
        if (0<=ny<n and 0<=nx<m) and graph[ny][nx] == 1:
            # 아직 방문되지 않은 정점이면
            if visited[ny][nx] == 0:
                # 큐에 삽입
                queue.append((ny, nx))

                # 이전에 방문한 정점의 방문 횟수를 누적해서 더하기
                visited[ny][nx] += visited[y][x] + 1
        
            if nx==m-1 and ny==n-1:
                print(visited[ny][nx])
                exit()

   


        
                 
    
            

