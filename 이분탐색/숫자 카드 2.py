import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def search_card(card, left, right):
    right_index = bisect_right(card, left)
    left_index = bisect_left(card, right)
    return right_index-left_index

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find_card = list(map(int, input().split()))
card.sort()

for i in range(m):
    print(search_card(card, find_card[i], find_card[i]), end=' ')
