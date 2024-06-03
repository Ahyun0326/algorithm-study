import sys
input = sys.stdin.readline

# 스위치의 수, 램프의 수
n, m = map(int, input().split())
lamp_status = [0 for _ in range(m+1)]
info = []
# 스위치에 대한 정보 입력 받기
for i in range(n):
    # 스위치와 연결된 램프의 수, 연결된 램프의 번호
    info.append(list(map(int, input().split())))
    for j in range(1, len(info[i])):
        # 켤 수 있는 스위치라면 1증가
        lamp_status[info[i][j]] += 1

for i in range(len(info)):
    tmp = lamp_status[:][:]
    for j in range(1, len(info[i])):
        tmp[info[i][j]] -= 1

    result = True
    # 하나의 스위치 껐을 때 모든 램프가 켜져 있다면 1 출력
    for j in range(1, len(tmp)):
        if tmp[j] == 0:
            result = False
    if result:
        print(1)
        exit()

print(0)

  
            

