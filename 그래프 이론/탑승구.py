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


# 탑승구의 수
g = int(input())
# 비행기의 수
p = int(input())

parent = [0] * (g+1)

for i in range(g+1):
    parent[i] = i

# 비행기가 도킹할 수 있는 탑승구의 정보 입력받기 
info_list = []
for i in range(p):
    info_list.append(int(input()))

result = 0
for info in info_list:

    # info 노드의 도킹 정보 확인
    root = find_parent(parent, info)
    
    # 집합의 루트 노드가 0이라면
    if root == 0:
        # 도킹이 불가능하므로 종료
        break

    # 집합의 루트 노드가 0이 아니라면
    # 왼쪽에 있는 집합과 합집합(union_parent) 연산 수행
    union_parent(parent, root-1, root)
    result += 1

print(result)
