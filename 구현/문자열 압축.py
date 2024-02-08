def solution(s):
    
    # 자를 문자열의 길이
    length = 1
    # 최대 문자열 길이
    result = len(s)
    
    # 자를 문자열의 개수가 전체 문자열의 절반을 넘어서면 반복문 종료
    while(length <= len(s)//2):
        
        i = length # 반복문 시작 인덱스를 자를 문자열의 길이로 지정
        
        s_list = [s[i:i+length] for i in range(0, len(s), length)]
        tmp_result = ""
        
        cnt = 1    # 두 문자열이 같을 때 값을 1 증가해주기 위한 변수
        for i in range(len(s_list)-1):
            
            final = s_list[i+1]
            
            if s_list[i] == s_list[i+1]:
                cnt += 1
            else:
                if cnt != 1:
                    tmp_result += str(cnt) + s_list[i]
                    cnt = 1
                else:
                    tmp_result += s_list[i]
        
        if cnt == 1:
            tmp_result += final
        else:
            tmp_result += str(cnt) + final
            
        result = min(result, len(tmp_result))
        length += 1
    
    return result
