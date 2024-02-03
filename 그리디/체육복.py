def solution(n, lost, reserve):
    
    # n: 총 학생 수
    # lost: 도난당한 학생 번호
    # reserve: 여분이 있는 학생 번호
    
    # 여벌 체육복을 가지고 있는 학생이 도난당한 경우는 제외
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    for i in _reserve:

        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)

    return n-len(_lost)
