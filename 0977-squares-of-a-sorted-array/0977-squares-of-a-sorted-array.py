class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        l = 0
        r = len(nums) - 1
        x = len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans[x] = nums[r]**2
                r -= 1
                x -= 1
            else:
                ans[x] = nums[l]**2
                l += 1
                x -= 1
        
        return ans