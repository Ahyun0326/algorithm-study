def solution(N, stages):

    answer = []
    
    cnt = len(stages) # 사용자의 도전 횟수
    tmp = []
    # 각 챌린지별 실패 횟수 카운트
    for i in range(1, N+1):
        
        fail = stages.count(i)        
        
        # 각 스테이지의 번호, 실패율 tmp에 추가
        if fail == 0:
            tmp.append([i, 0])
        else:
            if cnt != 0:
                tmp.append([i ,fail/cnt])
            else:
                tmp.append([i, 0])

        cnt -= fail # 사용자의 도전 횟수 감소
        
        
    # 각 스테이지의 번호를 실패율의 내림차순으로 정렬
    # 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
    tmp = sorted(tmp, key=lambda x:(-x[1], x[0]))
                 
    # 스테이지 번호만 남겨 answer에 추가
    for i in tmp:
        answer.append(i[0])
    
    return answer
