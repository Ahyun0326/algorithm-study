import sys

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

graph.sort()

choice = []
for i in range(len(graph)):
    
    if len(choice) == 0:
        choice.append(graph[i])

    elif len(choice) > 0:

        if choice[-1][1] > graph[i][1]:
            choice.pop()
            choice.append(graph[i])

        elif choice[-1][1] <= graph[i][0]:
            choice.append(graph[i])

print(len(choice))
