class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numss = set()
        for i in nums:
            if i in numss:
                return True
            else:
                numss.add(i)
        return False