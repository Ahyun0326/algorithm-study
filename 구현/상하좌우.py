import sys

n = int(sys.stdin.readline())
move = sys.stdin.readline().split()

start = [1,1]
for i in move:

    if i == 'U':
        if start[0]-1 < 1:
            continue
        start[0] -= 1
   
    elif i == 'D':
        if start[0]+1 >n:
            continue
        start[0] += 1
    
    elif i == 'L':
        if start[1]-1 < 1:
            continue
        start[1] -= 1        
    
    elif i == 'R':
        if start[1]+1 > n:
            continue
        start[1] += 1

print(start[0], start[1])
