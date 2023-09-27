import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

left = 0
right = max(arr)
result = 0
temp = 0

while left <= right:
    mid = (left+right)//2
    
    for i in arr: 
        temp += min(i, mid)
    
    if temp > m:
        right = mid-1
        temp = 0

    elif result < m:
        result = mid
        left = mid+1
        temp = 0

print(result)
