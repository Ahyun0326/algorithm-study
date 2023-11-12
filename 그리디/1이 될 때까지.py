import sys

n, k = map(int, sys.stdin.readline().split())

min = 0

while(True):

    if n == 1:
        break
    
    # n이 k로 나누어 떨어지면 n을 k로 나눈다.
    if n % k == 0:
        n = n//k
        min += 1
    else:
        n -= 1
        min += 1
        
print(min)
