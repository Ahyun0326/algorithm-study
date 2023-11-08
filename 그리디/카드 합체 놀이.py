import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

card.sort()

for i in range(m):

    # 제일 작은 카드 두 개를 꺼내기
    a = card.pop(0)
    b = card.pop(0)

    card_sum = a+b

    # 꺼낸 카드 두 개를 더해 리스트에 다시 넣기
    card.append(card_sum)
    card.append(card_sum)

    # 카드들을 다시 오름차순 정렬
    card.sort()
    
print(sum(card))
