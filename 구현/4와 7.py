k = int(input())

# format 함수를 이용해 숫자를 2 진수로 변환
s = format((k+1), 'b')
s = s[1::] # 맨 앞 자리수를 한 개 제거

for i in s:
    if(i == '0'):
        print('4', end='')
    elif(i == '1'):
        print('7', end='')
