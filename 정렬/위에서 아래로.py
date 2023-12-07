n = int(input())

nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

# 내림차순 정렬
nums.sort(reverse=True)

# 한 줄에 공백으로 구분하여 출력
for i in nums:
    print(i, end=' ')
