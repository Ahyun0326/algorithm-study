s = list(input())

alpha = []
digit = []
# 탐색 시작
for i in range(len(s)):

    # 문자라면 alpha 리스트에 추가
    if s[i].isalpha():
        alpha.append(s[i]) 

    # 숫자라면 digit 리스트에 추가
    elif s[i].isdigit():
        digit.append(int(s[i]))

# 모든 탐색이 끝났으면
# 문자만 들어 있는 리스트를 오름차순 정렬
alpha.sort()

# 숫자들의 총 합을 계산하여 문자가 있는 리스트의 마지막에 추가
alpha.append(str(sum(digit)))
# 리스트를 문자열로 변환
result = ''.join(alpha)

# 최종 결과 출력
print(result)
