import sys
input = sys.stdin.readline

# M명의 조카가 있고 N개의 과자가 있을 때 조카 1명에게 줄 수 있는 막대 과자의 최대 길이
# 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있찌만, 과자를 하나로 합칠 수는 없다.

# pypy 제출 

m, n = map(int, input().split())
snack = list(map(int, input().split()))

start = 1
end = max(snack)
result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for length in snack:
        if length < mid:
            continue
        else:
            cnt += length//mid
    if cnt < m:
        end = mid-1
    elif cnt >= m:
        start = mid+1
        result = mid

print(result)
