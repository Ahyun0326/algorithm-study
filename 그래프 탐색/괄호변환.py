import sys
sys.setrecursionlimit(10**6)

# 올바른 괄호 문자열인지 검사하는 함수
def check(u):
    
    stack = []
    
    # u가 올바른 괄호 문자열인지 검사
    for i in u:
         # 여는 괄호이면 스택에 삽입
        if i == '(':
            stack.append(i)
        # 닫는 괄호이면 현재 스택에 있는 여는 괄호 제거
        elif i == ')':
            # 스택이 비어있다면 올바른 괄호 문자열이 아니므로 종료
            if len(stack) == 0:
                return False
            stack.pop()
        
    # 반복문이 끝났는데 스택에 남아 있는 여는 괄호가 있을 경우, 균형잡힌 괄호 문자열
    if len(stack) > 0:
        return False
    
    # 스택에 남아 있는 여는 괄호가 없을 경우, 올바른 괄호 문자열
    elif len(stack) == 0:
        return True

# 두 균형잡힌 괄호 문자열로 분리하는 함수
def separation(p):
    
    open_cnt = 0 # 여는 괄호 카운트
    close_cnt = 0 # 닫는 괄호 카운트
    
    for i in range(len(p)):
        # 여는 괄호이면 여는 괄호 카운트 증가
        if p[i] == '(':
            open_cnt += 1
        # 닫는 괄호이면 닫는 괄호 카운트 증가
        elif p[i] == ')':
            close_cnt += 1
        # 여는 괄호와 닫는 괄호의 짝이 맞을 경우    
        if open_cnt == close_cnt:
            return i

def solution(p):

    answer = ''
    
    # 빈문자열이면 빈 문자열 반환
    if p == '':
        return answer
    
    # 문자열 w를 두 균형잡힌 괄호 문자열로 분리
    i = separation(p)
    u = p[:i+1]
    v = p[i+1:]
    
    
    # u가 올바른 괄호 문자열인지 검사
    a = check(u)
    
    # u가 올바른 괄호 문자열이면 그대로 두고, v에 대해 재귀적으로 수행
    if a == True:
        answer = u + solution(v)
        
    # u가 올바른 괄호 문자열이 아니라면 새로운 문자열 생성
    else:
        # 빈 문자열에 첫 번째 문자로 "("를 붙이기
        tmp = "("
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어 붙이기
        tmp += solution(v)
        # ")"를 다시 붙이기
        tmp += ")"
        # u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향 뒤집어서 뒤에 붙이기
        u = list(u)[1:-1]
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        tmp += "".join(u)
        
        # 생성된 문자열 반환
        answer += tmp
    
    return answer

