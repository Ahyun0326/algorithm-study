import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

result = []
for i in range(n-1):
    if n == 1:
        result.append(0)
        break
    result.append(sensor[i+1] - sensor[i])

result.sort(reverse=True)
for i in range(k-1):
    if n == 1:
        break
    
    result.pop(0)    

print(sum(result))
