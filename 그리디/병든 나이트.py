import sys

n, m = map(int, sys.stdin.readline().split())

# 세로가 1일 때 방문할 수 있는 최대 칸 수: 1
if n == 1:
    result = 1
# 세로가 2일 때 방문할 수 있는 최대 칸 수: 4와 (m+1)/2 중 작은 값
elif n == 2:
    result = min(4, (m+1)//2)
# 가로가 7 미만일 때 방문할 수 있는 최대 칸 수: 4와 M 중 작은 값
elif m < 7:
    result = min(4, m)
else:
    result = m-7+5

print(result)
