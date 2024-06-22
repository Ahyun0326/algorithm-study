import sys
input = sys.stdin.readline

n = int(input())
tip = []
for _ in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

result = 0
for i in range(n):
    tmp = tip[i] - i
    if tmp < 0:
        continue
    result += tmp

print(result)