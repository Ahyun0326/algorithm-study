import sys
max = 1000001

N = int(sys.stdin.readline())
dp = [1000000000] * max

dp[1] = 0
for i in range(1, N):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    if(i*2 < max):
        dp[i*2] = min(dp[i*2], dp[i]+1)
    if(i*3 < max):
        dp[i*3] = min(dp[i*3], dp[i]+1)

print(dp[N])
