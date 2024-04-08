import sys
input = sys.stdin.readline

# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수 입력 받기
k, n = map(int, input().split())
l = []
for _ in range(k):
    l.append(int(input()))

start = 1
end = max(l)
result = 0

# n개를 만들 수 있는 랜선의 최대 길이 출력
while (start <= end):
    mid = (start+end)//2
    total = 0
    # mid 값으로 랜선 자르기
    for length in l:
        if mid <= length:
            total += length//mid
            
    # 자른 랜선의 총합이 n보다 크다면
    if total >= n:
        result = mid
        start = mid+1        

    # 자른 랜선의 총합이 n보다 작거나 같다면
    else:
        end = mid-1
         
print(result)
