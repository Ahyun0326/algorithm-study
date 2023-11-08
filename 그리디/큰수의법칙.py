import sys

n, m, k = map(int, sys.stdin.readline().split())

number = list(map(int,sys.stdin.readline().split()))

# 내림차순 정렬
number.sort(reverse=True)

result = 0
for i in range(m):

    # 가장 큰 수가 중복되지 않는 경우
    if number.count(number[0]) == 1:
        
        # k번 더했을 경우 그 두 번째로 큰 수를 더하기
        if (i+1)%k == 0:
            result += number[1]
            continue

        # 제일 큰 수 더하기
        result += number[0]
    
    # 가장 큰 수가 중복되는 경우
    elif number.count(number[0]) >= 2:
        # k값에 상관없이 가장 큰 수 계속 더하기
        result += number[0] 

print(result)
