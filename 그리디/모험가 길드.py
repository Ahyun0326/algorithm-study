import sys

n = int(sys.stdin.readline())
fear = list(map(int, sys.stdin.readline().split()))

# 공포도가 큰 순서대로 정렬
fear.sort(reverse=True)

max_fear = fear[0]
i = 0
guild_cnt = 0
while True:
    
    if len(fear) == 0:
        if max_fear == i:
            guild_cnt += 1
        break
    
    # max_fear의 개수만큼 모험가 길드가 구성되면 cnt를 증가하고 max_fear를 바꾸기
    if max_fear == i:
        i = 0
        guild_cnt += 1
        max_fear = fear[0]
    
    fear.pop(0)
    i += 1
    
print(guild_cnt)
