import sys

formula = list(sys.stdin.readline().strip().split('-'))

min = 0
for i in range(len(formula)):
    if i == 0:
        add_list = sum(list(map(int, formula[i].split('+'))))
        min += add_list
    
    elif i != 0:
        if '+' not in formula[i]:
            min -= int(formula[i])
        else:
            add_list = sum(list(map(int, formula[i].split('+'))))
            min -= add_list

print(min)
