class Solution:
    def isValid(self, s: str) -> bool:
        #first create a dict mapping closing to opening
        dic = {
            '(':')',
            '[':']',
            '{':'}'
        }

        #create the stack
        stack = []

        for i in s:
            if i in dic:
                stack.append(i)
            elif stack and dic[stack[-1]] == i:
                stack.pop()
            else:
                return False
        
        if stack == []:
            return True