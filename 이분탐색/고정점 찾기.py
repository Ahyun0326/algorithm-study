n = int(input())
array = list(map(int, input().split()))

start = 0
end = n-1


while start <= end:
    mid = (start+end)//2

    # 인덱스 값과 mid가 동일하다면(고정점이라면)
    if array[mid] == mid:
        # 고정점 출력하고 종료
        print(mid)
        exit()

    # 현재 값이 mid보다 더 작다면 오른쪽 탐색
    elif array[mid] < mid:
        start = mid+1
    
    # 현재 값이 mid보다 더 크다면 왼쪽 탐색
    else:
        end = mid - 1

# 끝까지 고정점을 찾지 못했다면 -1 출력
print(-1)
