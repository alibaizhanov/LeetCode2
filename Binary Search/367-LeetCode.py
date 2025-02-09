class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        l = 0
        r = num
        
        while l<r:
            mid = int((l+r)/2)
            
            if mid*mid  == num:
                return True
            
            if mid*mid > num:
                r = mid
            else:
                l = mid+1
            
        return False