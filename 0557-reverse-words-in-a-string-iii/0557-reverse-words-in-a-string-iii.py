class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        r = 0
        
        s = [*s]
        print(s)
        
        while r < len(s) and l < len(s):
            while s[r] != ' ' and r < len(s) - 1:
                r += 1

            
            new = r 
            if r <len(s) - 1:            
                r = r -1
            
            while l < r:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
            
            l = new + 1
            r = new + 1
            
        
        return ''.join(s)