import sys

n, m = map(int, sys.stdin.readline().split())

card = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []
for i in range(n):

    result.append(min(card[i]))

print(max(result))

