import sys
sys.setrecursionlimit(10**6)

def dfs(curr):
    global cnt
    visited[curr] = True
    next = student[curr]

    if visited[next]:
        if not finished[next]:
            while(next!=curr):
                next = student[next]
                cnt += 1
            cnt += 1                    
    else:
        dfs(next)
    finished[curr] = True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    student = [0]
    student += list(map(int, sys.stdin.readline().split()))
    visited = [False for _ in range(n+1)]
    finished = [False for _ in range(n+1)] 

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    print(n-cnt)
