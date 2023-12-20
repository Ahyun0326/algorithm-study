def solution(stones, k):
    
    left = 1
    right = max(stones)
    
    while(left<=right):
        mid = (left+right)//2
        cnt = 0
        for i in stones:
             
            if (i-mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break

        if cnt >= k:
            right = mid-1
        else:
            left = mid+1
        
    return left
