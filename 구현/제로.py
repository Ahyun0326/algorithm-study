k = int(input())

list = []
for i in range(k):
    money = int(input())
    if(money == 0):
        list.pop()
        continue
    list.append(money)

result = 0
if not list:
    result = 0
elif list:
    result = sum(list)
print(result)
