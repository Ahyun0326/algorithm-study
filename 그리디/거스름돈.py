import sys

n = int(sys.stdin.readline())

cnt = 0

while n > 0:

    if n//500 > 0:
        cnt += n//500
        n %= 500

    elif n//100 > 0:
        cnt += n//100
        n %= 100

    elif n//50 > 0:
        cnt += n//50
        n %= 50
    
    elif n//10 > 0:
        cnt += n//10
        n %= 10

print(cnt)
