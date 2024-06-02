import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().strip()))

result = []
for a in range(n-7):
    for b in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        cnt1 += 1
                    if board[i][j] != 'B':
                        cnt2 += 1
                else:
                    if board[i][j] != 'B':
                        cnt1 += 1
                    if board[i][j] != 'W':
                        cnt2 += 1
        result.append(min(cnt1, cnt2))

print(min(result))