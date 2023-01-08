class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window
        left = 0
        right = 0
        curr_sum = 0
        max_sum = -1000000000000
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            while curr_sum < 0:
                curr_sum -= nums[left]
                left += 1
            right += 1
            
        
        return max_sum