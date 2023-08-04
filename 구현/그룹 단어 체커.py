n = int(input())
result = [True] * n
word_list = []

for i in range(n):
    s = input()

    word_list.append(list(s))


for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        if word_list[i].count(word_list[i][j]) == 1:
            continue
        elif word_list[i].count(word_list[i][j]) > 1:

            if j+1 == len(word_list[i]):
                break

            # 다음 인덱스 위치 조사 
            # 다음 인덱스 위치와 현재 인덱스 위치의 차이가 1보다 크다면 불연속 글자            
            try:
                next_index = word_list[i].index(word_list[i][j], j+1, len(word_list[i]))
            except:
                continue
            
            if next_index - j > 1:
                result[i] = False
                break
            elif next_index - j == 1:
                continue

print(result.count(True))
