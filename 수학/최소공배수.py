import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    
    while(b != 0):
        r = a%b
        a = b
        b = r
    return a

for i in range(t):

    a, b = map(int, input().split())

    # 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수로 나눈 것과 같다.
    result = gcd(a, b)
    result = (a*b) // result
    print(result)
