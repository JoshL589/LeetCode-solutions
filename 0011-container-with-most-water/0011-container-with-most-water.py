class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_vol = 0
        while l < r:
            curr_vol = min(height[l], height[r]) * (r - l)
            max_vol = max(max_vol, curr_vol)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol