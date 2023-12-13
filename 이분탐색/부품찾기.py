import sys

def binary_search(target, store, start, end):
    start = 0
    end = len(store)
    while start <= end:
        
        mid = (start+end) // 2
        # 고객이 찾는 부품이 있다면 yes 출력
        if store[mid] == i:
            print("yes", end=' ')
            return
        # 고객이 찾는 부품이 크면 오른쪽 탐색 
        elif store[mid] < target:
            start = mid+1
        # 고객이 찾는 부품이 작으면 왼쪽 탐색
        else:
            end = mid-1
    # 고객이 찾는 부품이 없으면 no 출력
    print("no", end= ' ')
    return


n = int(sys.stdin.readline())
store = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
customer = list(map(int, sys.stdin.readline().split()))

# 가게에 있는 부품의 번호 오름차순 정렬
store = sorted(store)
for i in customer:
    binary_search(i, store, 0, n-1)

