import sys

n = int(sys.stdin.readline())
chain = list(map(int, sys.stdin.readline().split()))

# 체인 오름차순 정렬
chain.sort()
tiredchains = 1
chaincount = n

# n만큼 반복
for i in range(n):

    if tiredchains + chain[i] >= chaincount:
        break
    else:
        tiredchains += chain[i]
        chaincount -= 1

print(chaincount-1)
