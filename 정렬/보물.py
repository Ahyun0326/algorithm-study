n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a, key = lambda x:x)
d = sorted(b, key = lambda x:x, reverse=True)

s = []
# a 리스트에서 제일 작은 값부터 b의 큰 값과 매치시키기
for i in range(len(d)):
    s.append([c[i], d[i]])

result = b
for i in range(len(s)):
    if s[i][1] in b:
        pos = b.index(s[i][1])
        result[pos] = [s[i][0], result[pos]]

sum = 0
for i in range(len(result)):
    mul = result[i][0] * result[i][1]
    sum += mul

print(sum)
