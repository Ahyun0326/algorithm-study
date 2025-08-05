import sys

n = int(sys.stdin.readline())
scores = []
for i in range(n):
    scores.append(int(sys.stdin.readline()))

cnt = 0
for i in range(n-1, 0, -1):
    if scores[i-1] >= scores[i]:
        cnt += scores[i-1] - (scores[i]-1)
        scores[i-1] = scores[i]-1

print(cnt)