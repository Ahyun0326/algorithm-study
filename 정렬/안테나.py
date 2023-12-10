import sys

n = int(sys.stdin.readline())

house = list(map(int, sys.stdin.readline().split()))

#오름차순 정렬
house = sorted(house)

# 중앙 값 계산
# 집의 개수가 짝수일 경우 중앙 값이 두 개
if n % 2 == 0:
    mid1 = n//2 - 1
    mid2 = n//2
    
    distance1 = list(map(lambda x:abs(x-house[mid1]), house))
    distance2 = list(map(lambda x:abs(x-house[mid2]), house))

    if distance1 <= distance2:    
        print(house[mid1])
    else:
        print(house[mid2])

# 집의 개수가 홀수일 경우 중앙 값이 한 개
else:
    mid = n//2
    print(house[mid])



