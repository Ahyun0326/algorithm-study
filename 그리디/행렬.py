import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# a, b 행렬을 비교한 정보를 array 리스트에 저장
array = [[False for _ in range(m)] for _ in range(n)] 
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            continue
        array[i][j] = True

cnt = 0

# 반례
if n < 3 and m < 3:
    # 3x3보다 작고 두 행렬이 다르다면 -1
    if a != b:
        print(-1)
        exit(0)
    # 3x3보다 작고 두 행렬이 같다면 0
    else:
        print(0)
        exit(0)
else:
    for i in range(n-2):
        for j in range(m-2):
           # 두 행렬이 같지 않다면
           if array[i][j] == False:
                # 3x3 만큼 행렬의 값 뒤집기
                for x in range(i, i+3):
                   for y in range(j, j+3):
                        if array[x][y] == True:
                           array[x][y] = False
                        else:
                           array[x][y] = True
                cnt += 1

# 결과 배열 확인     
for i in range(n):
    for j in range(m):
        # False인 값이 하나라도 있다면 같게 만들 수 없으므로 -1 출력
        if array[i][j] == False:
            print(-1)
            exit(0)

print(cnt)                       

