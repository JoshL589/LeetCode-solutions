
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        result = 0
        maxcount = 0
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] > maxcount:
                result = i
                maxcount = count[i]
                
        return result
        