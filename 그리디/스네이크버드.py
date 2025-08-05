import sys

# 과일의 개수, 스네이크버드 초기 길이
n, l = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
height.sort()

for i in range(n):
    if l >= height[i]:
        l += 1
print(l) 