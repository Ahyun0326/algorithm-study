def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# 여행지의 연결 정보를 담은 행렬
graph = [list(map(int, input().split())) for _ in range(n)]

# 행렬 탐색하며 연결정보 확인
for i in range(len(graph)):
    for j in range(len(graph)):
        # 서로 연결되어 있다면
        if graph[i][j] == 1:
            # 합집합 연산 수행
            union_parent(parent, i+1, j+1)

# 여행 계획 입력 받기
plan = list(map(int, input().split()))

# 첫 번째 plan의 루트 노드 값 구하기
root = find_parent(parent, plan[0])

# 여행 계획에 속하는 노드의 루트 노드가 동일한지 확인
for i in range(1, len(plan)):
    # 루트 노드가 같다면 continue
    if find_parent(parent, i) == root:
        continue
    # 루트 노드가 같지 않다면 "NO"를 출력하고 프로그램 종료
    else:
        print("NO")
        exit()

# 루트 노드가 같은 경우 "YES" 출력
print("YES")
