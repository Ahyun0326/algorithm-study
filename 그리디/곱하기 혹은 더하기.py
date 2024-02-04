# 공포도가 X인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참가해야 여행을 떠날 수 있도록 규정 

# 모험가의 수 입력받기
n = int(input())

# 모험가 리스트 입력받기
adventurer = list(map(int, input().split()))

# 공포도가 가장 작은 학생 순으로 모험가 리스트 정렬
adventurer.sort()

result = 0
cnt = 0  
i = 0

# 공포도가 작은 수만큼 차례대로 그룹 생성
while(cnt <= n):

    # 현재 모험가의 공포도 구해서 cnt에 누적
    cnt += adventurer[i]

    # 현재 모험가의 공포도보다 더 큰 값이 범위 내에 있다면  
    if max(adventurer[i:cnt]) > adventurer[i]:
        break   # 반복문 종료
    
    # 그렇지 않다면
    result += 1         # 그룹에 추가
    i += adventurer[i]  # 인덱스를 현재 모험가의 공포도만큼 증가

# 결과 출력      
print(result)
