s = list(map(int, input()))

total = len(s) # 문자열의 총 길이 계산

zero_cnt = 0 # 연속된 0의 개수 계산
one_cnt = 0
# s만큼 반복
for i in range(0, len(s)):
    # 현재 문자가 0이면 continue
    if s[i] == 0:
        continue
    # 현재 문자가 1이고, 이전 문자가 0이면
    elif s[i] == 1 and s[i-1] == 0:
        zero_cnt += 1 # zero_cnt 증가

# 연속된 1의 개수 개산
one_cnt = total - zero_cnt

if one_cnt > zero_cnt:
    print(zero_cnt)
elif one_cnt < zero_cnt:
    print(one_cnt)
else:
    print(zero_cnt)
