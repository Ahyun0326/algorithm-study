import sys
import heapq

n = int(sys.stdin.readline())

q = []
hq = []
for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    q.append([s,t])

q.sort()

heapq.heappush(hq, q[0][1]) # 우선순위 큐에 끝나는 시간 삽입

for i in range(1, n):

    # 우선순위 큐의 끝나는 시간보다 큐의 강의 시작 시간이 더 빠르면 
    if q[i][0] < hq[0]: 
        heapq.heappush(hq, q[i][1]) # 해당 강의의 끝나는 시간 삽입

    else:
        heapq.heappop(hq)
        heapq.heappush(hq, q[i][1])

print(len(hq))
