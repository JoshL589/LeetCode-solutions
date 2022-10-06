class Solution:
    def isValid(self, s: str) -> bool:
        
        opposite = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        
        for i in s:
            if i in opposite:
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif i == opposite[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False