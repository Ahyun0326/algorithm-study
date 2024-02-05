n, m = map(int, input().split())

k = list(map(int, input().split()))

num = []
for i in range(len(k)):
    # 같은 무게의 공이 1개 이상이면
    if k.count(k[i]) > 1:
        # num에 해당하는 공의 번호가 없다면 추가
        if k[i] not in num:
            num.append(k[i])

# n이 1일 경우 서로 다른 공을 고를 수 없으므로 0 
if n == 1:
    result = 0
# 1이 아닐 경우 nC2 - 중복되는 공의 개수
else:
    result = (n*(n-1))//2 - len(num)

# 결과 출력
print(result)
