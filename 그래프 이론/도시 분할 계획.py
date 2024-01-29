import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):

  # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 집의 개수, 길의 개수 입력 받기
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 리스트
edges = []
result = []

# 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
  parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(m):
  a, b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost, a, b))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
  cost, a, b = edge

  # 사이클이 발생하지 않았다면
  if (find_parent(parent, a) != find_parent(parent, b)):
    # 같은 집합에 포함시키기
    union_parent(parent, a, b)
    result.append(cost) # result 리스트에 현재 비용 추가

# 저장된 비용 중 가장 비용이 큰 간선 제거
result.remove(max(result))
# 길의 유지비 합의 최소값 출력
print(sum(result))
