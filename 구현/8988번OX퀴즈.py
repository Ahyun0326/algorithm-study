'''
O이면, 처음 시작하거나 이전에 X가 있었다면 점수가 1부터 시작
X이면, 점수가 모두 0으로 동일
'''

num = int(input())
result_list = []
for i in range(num):
    result = input()
    result_list.append(list(result)) #입력 받은 문자열을 한 글자씩 분리

# 입력한 테스트케이스 개수만큼 반복
score = []
for i in range(len(result_list)):
    score_sum = 0
    cnt = 0
    tmp_result = result_list[i]
    for j in tmp_result:
        if j == 'O':
            cnt += 1
            # 'X'가 나오기 전까지 반복하여 score_sum에 1씩 증가하여 더하기
            score_sum += cnt
        elif j == 'X': #'X'가 나오면 cnt 값 0으로 초기화 후 다시 반복문으로 돌아가기
            cnt = 0
            continue
    score.append(score_sum)

for i in score:
    print(i)
