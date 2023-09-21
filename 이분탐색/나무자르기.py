import sys

n, m = map(int, sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(height)
while(left+1 < right):
    mid = (left+right)//2
    sum = 0
    for i in range(n):
        if height[i] > mid:
            sum += height[i] - mid 
    
    if sum >= m:
        left = mid
    elif sum < m:
        right = mid

print(left)
