class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hashmap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for char in s:
            if char in hashmap:
                stack.append(char)
                continue
            if stack != [] and char == hashmap[stack[-1]]:
                stack.pop()
                continue
            else:
                return False
        if stack == []:
            return True