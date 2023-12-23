import sys

# 원생들의 수, 조의 개수 입력받기
n, k = map(int, sys.stdin.readline().split())
# 원생들의 키를 원생들의 수만큼 입력받기
kids = list(map(int, sys.stdin.readline().split()))

sub = []
for i in range(n-1):
    sub.append(kids[i+1] - kids[i])

sub.sort()
print(sum(sub[0:n-k]))
