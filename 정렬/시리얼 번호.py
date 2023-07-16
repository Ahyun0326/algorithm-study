n = int(input())

s = []
for i in range(n):
    line = input()
    s.append(line)

digit_sum = [0 for _ in range(n)]

#자릿수의 합 구하기
for i in range(len(s)):
    if s[i].isalpha():
        s[i] = [s[i], digit_sum[i]]
    else:
        tmp = list(s[i]) #알파벳이 아닌 것들을 한 글자씩 분리해 저장
        for j in tmp:
            if j.isdigit():
                digit_sum[i] += int(j)
        s[i] = [s[i], digit_sum[i]]

s.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for i in s:
    print(i[0])
