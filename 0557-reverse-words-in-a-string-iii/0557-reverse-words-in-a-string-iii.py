class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        ans = []
        for i in s:
            l = 0
            r = len(i) - 1
            i = list(i)
            
            while l < r:
                temp = i[l]
                i[l] = i[r]
                i[r] = temp
                l += 1
                r -= 1

            i = ''.join(i)

            ans.append(i)
        return ' '.join(ans)