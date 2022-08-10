class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = []
        
        for i in str(x):
            num.append(i)

        if num == num[::-1]:
            return True
        
        return False
        