n = int(input())

time = list(map(int, input().split()))

time.sort(key=lambda x:x)
tmp = 0
sum = 0
for i in time:
    tmp += i
    sum += tmp

print(sum)
