import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    # a, b 입력 받기
    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))

    # a, b 리스트 내림차순 정렬
    A.sort()    
    B.sort()

    start = 0
    cnt = 0

    for j in range(n):
        while True:
            if start == m or A[j]<=B[start]:
                cnt += start
                break
            else:
                start += 1

    print(cnt)
