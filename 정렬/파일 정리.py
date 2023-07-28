import sys

n = int(sys.stdin.readline().rstrip('\n'))

d = dict()
for _ in range(n):
    file = sys.stdin.readline().rstrip('\n')
    file = file.split('.')
    if not file[1] in d:
        d[file[1]] = 1
    else:
        d[file[1]] += 1

result = sorted(d.items())
for i in result:
    print(i[0], end = ' ')
    print(i[1])
