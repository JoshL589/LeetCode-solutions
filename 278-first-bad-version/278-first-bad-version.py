# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        
        #will stop when l >= r
        while l < r: 
            #mid point
            m = (l + r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l
            
        