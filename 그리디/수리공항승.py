import sys

# 물이 새는 곳의 개수, 테이프의 길이
n, l = map(int, sys.stdin.readline().split())

# 물이 새는 위치
water = list(map(int, sys.stdin.readline().split()))

water.sort()
start = water[0]
cnt = 1
for location in water[1:]:
    if location in range(start, start+l):
        continue
    else:
        start = location
        cnt += 1

print(cnt)
