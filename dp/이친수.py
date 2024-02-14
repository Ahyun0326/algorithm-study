dp =[0 for _ in range(90)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
n = int(input())

for i in range(3, n):
    if dp[i] == 0:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1])
