cnt = 0 

def dfs(i, data, numbers, target):
    
    global cnt
    if i == len(numbers):
        if data == target:
            cnt += 1
        return
    
    dfs(i+1, data-numbers[i], numbers, target)
    dfs(i+1, data+numbers[i], numbers, target)
    
def solution(numbers, target):
    
    dfs(0, 0, numbers, target)
    return cnt

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
