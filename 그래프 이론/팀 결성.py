# 0 a b: a번 학생이 속한 팀과 b번 학생이 속한 팀을 합침
# 1 a b: a번 학생과 b번 학생이 같은 팀에 속해있는지 확인

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

# 학생의 번호, 연산의 개수 입력 받기
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
  parent[i] = i

# 각 연산을 하나씩 확인
for _ in range(m):
  calculate, a, b = map(int, input().split())
  # 0이라면 합집합(union) 연산
  if calculate == 0:
    union_parent(parent, a, b)
  # 1이라면 찾기(find) 연산
  elif calculate == 1:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 같은 팀에 속해있다면 YES 출력
    if a == b:
      print("YES")
    # 같은 팀에 속해있지 않다면 NO 출력  
    else:
      print("NO")
