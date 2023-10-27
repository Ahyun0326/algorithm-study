import sys

n = int(sys.stdin.readline())
homework = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

homework.sort()
tmp = []
result = 0
for date in range(n, 0, -1):
    while homework and homework[-1][0] >= date:
        tmp.append(homework.pop()[1])
    if tmp:
        tmp.sort()
        result += tmp.pop()

print(result)
