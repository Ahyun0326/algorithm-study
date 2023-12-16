import sys

# 집의 개수, 공유기의 개수 입력
n, c = map(int, sys.stdin.readline().split())

# 집의 좌표 n개 입력받기
home = []
for i in range(n):
    home.append(int(sys.stdin.readline()))

# 집들의 위치를 오름차순으로 정렬
home = sorted(home)

# 집들 사이의 최소 거리와 최대 거리 계산
start = max(home)
for i in range(n-1):
    if (home[i+1] - home[i]) < start:
        start = home[i+1] - home[i] 

end = max(home) - min(home)
result = 1

# start가 end보다 작거나 같다면 반복
while start <= end:

    # 집들 사이의 최소 거리와 최대 거리의 중앙 값 이용
    mid = (start+end)//2

    cnt = 1
    pos = 0
    # 구한 mid 기준으로 현재 집에서 다음 집의 거리가 mid 이상인 경우 공유기 설치 가능
    for i in range(1, n):
        # 두 집의 거리 치아기 mid 이상이라면 공유기 설치
        if (home[i] - home[pos]) >= mid: 
            cnt += 1
            pos = i

    # 공유기의 개수가 C 미만이면
    if cnt < c:
        # 공유기의 간격 좁히기
        end = mid-1
    # 공유기의 개수가 C 이상이면
    else:
        # 현재의 gap(mid) 저장
        result = mid
        # 공유기의 간격 늘리기
        start = mid+1

print(result)
