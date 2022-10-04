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
            elif stack != [] and char == hashmap[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True