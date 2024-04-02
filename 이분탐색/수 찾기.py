import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
find_array = list(map(int, input().split()))

# array 오름차순 정렬
array.sort()
for i in range(m):
    start = 0
    end = n-1 
    find = False
    # 이분탐색 수행
    while (start <= end): 
        
        # 중앙 값 계산
        mid = (start+end)//2
        
        # 찾고자 하는 값보다 작은 경우 오른쪽 탐색 
        if array[mid] < find_array[i]:
            start = mid + 1

        # 찾고자 하는 값보다 큰 경우 왼쪽 탐색
        elif array[mid] > find_array[i]:
            end = mid - 1

        else:
            print(1)
            find = True
            break
   
    if not find:
        print(0)
