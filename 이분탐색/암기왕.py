import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for i in range(m):
        start = 0
        end = n-1
        find = False
        while(start <= end):
        
            mid = (start+end)//2

            if note2[i] == note1[mid]:
                print(1)
                find = True
                break

            elif note2[i] < note1[mid]:
                end = mid-1

            elif note2[i] > note1[mid]:
                start = mid+1

        if not find:
            print(0)
