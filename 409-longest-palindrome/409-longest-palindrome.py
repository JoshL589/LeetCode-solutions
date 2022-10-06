class Solution:
    def longestPalindrome(self, s: str) -> int:
        sCounter=Counter(s)
        print(sCounter)
        odd=False
        maxlen=0
        for val in sCounter.values():
            if val%2 == 0:
                maxlen += val
            else:
                maxlen += val//2 * 2
                odd = True
        if odd:
            return maxlen + 1
        else: 
            return maxlen