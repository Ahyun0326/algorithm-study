n = int(input())

k =[]
for i in range(n):
    k.append(i+1)

result = []
while len(k)-1 != 0:
    result.append(k.pop(0))
    k.append(k.pop(0)) 

result.append(k.pop(0))

for i in result[0::]:
    print(i, end=' ')  
