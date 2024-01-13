import heapq
INF = int(1e9)

# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시 입력 받기
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]    
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # x에서 y 도시로 메시지가 전달되는 시간이 Z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 정점 탐색
        for i in graph[now]:
            # 인접한 정점으로 이동하기 위한 거리 계산
            cost = dist + i[1]

            # 현재 노드를 거쳐 다음 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 최단 경로 업데이트
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c) # 도시 c에서 출발

cnt = 0
time = 0
for i in range(1, n+1):
    # 도달할 수 없는 경우이거나 i가 c라면 continue
    if distance[i] == INF or i == c:
        continue
    # 도달할 수 있는 경우 cnt 1 증가
    else:
        cnt += 1
        if distance[i] > time:
            time = distance[i]

# 결과 출력
print(cnt, time)
