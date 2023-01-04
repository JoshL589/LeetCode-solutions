class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0

        r = len(nums) - 1

        x = len(nums) - 1

        ans = len(nums) * [0]

        while l <= r:

            if (abs(nums[l]) > abs(nums[r])):

                ans[x] = nums[l]**2

                x -= 1

                l += 1

            else:

                ans[x] = nums[r]**2

                x -= 1

                r -= 1

        return ans