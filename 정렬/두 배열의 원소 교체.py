n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순으로 정렬
A = sorted(A)
# B는 내림차순으로 정렬
B = sorted(B, reverse=True)

# K번 반복하여 A, B의 원소 스와핑
for i in range(k):
    # A의 원소가 B의 원소보다 작을 경우에만 바꾸기
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

# 배열 A의 모든 원소의 합 출력
print(sum(A))
