import sys
input = sys.stdin.readline

t = int(input())
d = {1:1,2:2,3:4}
num = []
for _ in range(t):
    num.append(int(input()))

for i in range(4, 1000001):
    d[i] = (d[i-3] + d[i-2] + d[i-1]) % 1000000009

for i in range(t):
    print(d[num[i]])