import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    find = {}
    for i in note1:
        find[i] = 1

    for i in note2:
        num = find.get(i)
        if num == None:
            print(0)
        else:
            print(1)
