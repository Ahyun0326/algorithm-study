import sys
input = sys.stdin.readline

n = int(input())
num = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0
# 반복 횟수 계산
for _ in range(0, n, 2):    
    cnt += 1

value = n*n 
pos = 0
square_len = n-1
for i in range(cnt):

    if square_len == 0:
        graph[i][i] = value
        break

    # 아래로 이동
    for j in range(i, square_len+i):
        graph[j][i] = value
        value -= 1

    # 오른쪽으로 이동
    for j in range(i, square_len+i):
        graph[square_len+i][j] = value
        value -= 1

    # 위로 이동
    for j in range(square_len+i, i, -1):
        graph[j][square_len+i] = value
        value -= 1

    # 왼쪽으로 이동
    for j in range(square_len+i, i, -1):
        graph[i][j] = value
        value -= 1
        
    square_len -= 2

for i in range(len(graph)):
    for j in range (len(graph[i])):
        print(graph[i][j], end=' ')
    
        if num == graph[i][j]:
                pos = (i, j)

    print()

print(pos[0]+1, pos[1]+1)
