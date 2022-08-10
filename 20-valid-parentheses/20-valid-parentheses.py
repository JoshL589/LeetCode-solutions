class Solution:
    def isValid(self, s: str) -> bool:
        
        thing = []
        opposite = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        left = ['(','{','[']
        right = [')','}',']']
        
        
        for char in s:
            if len(thing) == 0 and char in right:
                return False
            if char in left:
                thing.append(char)
            else:
                if thing[-1] == opposite[char]:
                    thing.pop()
                else:
                    return False
                
        if thing == []:
            return True
        else:
            return False