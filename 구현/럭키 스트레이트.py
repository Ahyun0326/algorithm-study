n = list(map(int,input())) # 입력 받은 값을 리스트로 변환

# n을 반으로 나누기
medium = len(n)//2

#앞 부분과 뒤 부분의 합 계산
first = sum(n[0:medium])
second = sum(n[medium::])

if first == second:
    print("LUCKY")
else:
    print("READY")
