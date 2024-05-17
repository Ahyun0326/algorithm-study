import sys
input = sys.stdin.readline

def dfs(data):
    if len(data) == m:
        print(*data)
        return

    for i in range(len(array)):
        data.append(array[i])
        dfs(data)
        data.pop()

n, m = map(int, input().split())
array = sorted(set(list(map(int, input().split()))))
data = []
dfs(data)