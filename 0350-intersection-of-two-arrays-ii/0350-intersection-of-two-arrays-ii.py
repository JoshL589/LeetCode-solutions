class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic2 = {}
        
        for i in nums2:
            dic2[i] = dic2.get(i, 0) + 1
        
        ans = []
        
        for i in nums1:
            if i in dic2 and dic2[i] > 0:
                ans.append(i)
                dic2[i] -= 1
                
        
        return ans