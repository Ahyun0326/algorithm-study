import sys
input = sys.stdin.readline

n = int(input()) # 굴다리의 길이
m = int(input()) # 가로등의 개수
x = list(map(int, input().split())) # 설치 가능한 가로등의 위치 (오름차순)

result = x[0]
prev = 0
for i in range(m):
    if (x[i]-prev)%2 == 0:
        result = max(result, (x[i]-prev)//2)
    else:
        result = max(result, (x[i]-prev)//2+1)

    prev = x[i]

result = max(result, n-prev)
print(result)