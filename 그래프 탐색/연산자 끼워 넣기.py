# 수열의 개수 입력
n = int(input())
# 수열 정보 입력 받기
sequence = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 순으로 입력 받기
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화
max_value = int(-1e9)
min_value = int(1e9)

# dfs 함수
def dfs(i, now):
    global add, sub, mul, div, max_value, min_value

    # 모든 연산자를 사용한 경우, 최대값과 최솟값 업데이트
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    # 모든 연산자를 사용하지 않았을 경우 
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + sequence[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - sequence[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * sequence[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / sequence[i]))
            div += 1

# dfs 수행
dfs(1, sequence[0])

# 최대값과 최솟값 출력
print(max_value)
print(min_value)
