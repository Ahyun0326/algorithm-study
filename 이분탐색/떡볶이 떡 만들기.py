import sys

n, m = map(int,sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# array 오름차순 정렬
array = sorted(array)

start = 0
end = max(array)

result = 0
while start <= end:

    length = 0
    mid = (start+end)//2

    # 떡을 지정한 절단기의 높이만큼 자르기
    for i in array:
        # 현재 떡이 지정한 절단기의 높이보다 작다면
        if i <= mid:
            # 잘린 떡의 길이 0
            continue
        # 현재 떡이 지정한 절단기의 높이보다 크다면
        else:
            # 떡을 절단기로 자르기
            length += i-mid

    # 떡의 양이 부족한 경우 더 많이 자르기 
    if length < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid + 1

print(result)
