def solution(answers):
    
    answer = [0 for i in range(3)]
    
    num1 = []
    cnt = 1
    # 첫 번쩨 수포자가 찍은 값 저장
    for i in range(len(answers)):
        num1.append(cnt)
        cnt += 1
        
        if cnt == 6:
            cnt = 1

    num2 = []
    cnt = 1
    
    # 두 번째 수포자가 찍은 값 저장
    for i in range(len(answers)):
        
        # i가 짝수면 2 저장
        if i%2 == 0:
            num2.append(2)
        else:
            num2.append(cnt)
            # 카운트 증가
            cnt += 1
        
        # cnt가 2일 경우 3으로 변경
        if cnt == 2:
            cnt = 3
        # cnt가 6일 경우 1로 변경
        elif cnt == 6:
            cnt = 1
    
    num3 = []
    cnt = 1
    # 세 번째 수포자가 찍은 값 저장
    for i in range(len(answers)):

        if cnt == 11:
            cnt = 1
        
        if cnt < 3:
            num3.append(3)
            cnt += 1
        
        elif 3 <= cnt < 5:
            num3.append(1)
            cnt += 1
        
        elif 5 <= cnt < 7: 
            num3.append(2)
            cnt += 1
        
        elif 7 <= cnt < 9:
            num3.append(4)
            cnt += 1
            
        elif 9 <= cnt < 11:
            num3.append(5)
            cnt += 1
    
    # 정답과 수포자들이 찍은 값 비교
    for i in range(len(answers)):
        if answers[i] == num1[i]:
            answer[0] += 1
        if answers[i] == num2[i]:
            answer[1] += 1
        if answers[i] == num3[i]:
            answer[2] += 1
    
    max_score = max(answer)
    result = []
    for i in range(len(answer)):
        
        if max_score == answer[i]:
            result.append(i+1)
    
    return result
