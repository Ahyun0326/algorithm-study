import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = input().split()

    cnt1 = n.count('1')
    cnt2 = m.count('1')

    result = 0
    if cnt1 == cnt2:
        for i in range(len(n)):    
            if n[i] == '1' and m[i] == '0':
                result += 1
        print(result)
        continue
    
    elif cnt1 < cnt2:   # n의 1의 개수가 더 작은 경우
        for i in range(len(n)):
            if n[i] == '1' and m[i] == '0':
                result += 1
        print(result+(cnt2-cnt1))
        continue

    else:   # m의 1의 개수가 더 작은 경우
        for i in range(len(n)):
            if m[i] == '1' and n[i] == '0':
                result += 1
        print(result+(cnt1-cnt2))
        continue