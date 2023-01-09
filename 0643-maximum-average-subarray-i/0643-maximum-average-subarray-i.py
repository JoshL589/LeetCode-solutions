class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k - 1
        curr = 0
        
        for i in range(k):
            curr += nums[i]
            
        ans = curr/k
        
        for i in range(k, len(nums)):
            curr -= nums[i -k]
            curr += nums[i]
            ans = max(ans, curr/k)
            
        return ans