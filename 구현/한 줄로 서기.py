n = int(input())
num_list = list(map(int, input().split()))
result = [0 for i in range(n)]

for i in range(len(num_list)):
    if i == 0:
        result[num_list[i]] = 1
    else:
        num = num_list[i]
        pos_list = []
        for j in range(len(num_list)):
            if result[j] == 0:
                pos_list.append(j)
        result[pos_list[num_list[i]]] = i+1 

for i in result:
    print(i, end=' ')
