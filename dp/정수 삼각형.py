n = int(input())
dp = []

for i in range(n):
    line = list(map(int, input().split()))
    dp.append(line)

for i in range(1, len(dp)):
    for j in range(len(dp[i])):

        # 대각선 왼쪽에서 오는 경우
        if j == 0:
            left = 0 
        else:
            left = dp[i-1][j-1] + dp[i][j]

        # 대각선 오른쪽에서 오는 경우
        if j == len(dp[i])-1:
            right = 0
        else:
            right = dp[i-1][j] + dp[i][j]

        dp[i][j] = max(dp[i][j], left, right)

print(max(dp[n-1]))
