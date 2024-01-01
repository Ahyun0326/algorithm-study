n = int(input())
store = list(map(int, input().split()))

dp = [0] * 100
dp[0] = store[0]
dp[1] = max(store[0], store[1])

for i in range(2, n):

    dp[i] = store[i] + dp[i-2]

    # 현재 선택된 창고와 인접한 곳이 이미 약탈당했다면
    if dp[i-1] != 0:
        dp[i] = max(dp[i], dp[i-1]) # 둘 중에서 큰 값을 저장

print(dp[n-1])
