# 특정 원소가 속한 집합을 찾가
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())

parent = [0] * n

for i in range(n):
    parent[i] = i

# 모든 간선을 담을 리스트
edges = []

# 도로에 대한 정보 입력 받기
for _ in range(m):
    # x와 y번 집 사이에 양방향 도로가 있으며, 그 길이는 z
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

# 간선을 비용순으로 정렬
edges.sort()

total = 0   # 모든 간선들의 합 저장할 변수
result = 0  # 크루스칼 결과 간선들의 합 저장할 변수

# 간선들을 하나씩 확인
for edge in edges:
    cost, a, b = edge

    # 모든 간선들의 합 저장
    total += cost

    # 사이클이 속해있지 않은 경우에만 집합에 추가
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 절약할 수 있는 죄대 금액 = 모든 간선의 합 - 크루스칼 결과 간선의 합
print(total-result)
