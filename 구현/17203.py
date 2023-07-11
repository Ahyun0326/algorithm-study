n, q = map(int, input().split())

tmp = input()  
list = tmp

list = list.split()

result = []
for i in range(q):
    first, end = map(int, input().split())
    sum = 0
    for j in range(first-1, end-1):
        change = int(list[j+1]) - int(list[j])
        if change < 0:
            change = -change
        sum += change
    result.append(sum)

for i in result:
    print(i)
