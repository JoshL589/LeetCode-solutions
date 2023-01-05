class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            letters[i] = letters.get(i, 0) + 1
        
        for i in ransomNote:
            if i not in letters or letters[i] == 0:
                return False
            else:
                letters[i] -= 1
        
        return True
            
            