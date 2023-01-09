class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        ans = 0
        curr1 = 0
        curr0 = 0
        
        #while right hasnt reached end
        while r < len(nums):
            
            #update max
            ans = max(ans, curr1)
            
            #if 0, add to 0 counter
            if nums[r] == 0:
                curr0 += 1
                
                
            #auto matically add to 1 counter and increment r
            curr1 += 1
            r += 1
            
            #while too many zeros, decrease amount of zeros by reducing window size and increment l
            while curr0 > k:
                if nums[l] == 0:
                    curr0 -= 1
                curr1 -= 1
                l += 1
                
            #update max
            ans = max(ans, curr1)
        return ans
            