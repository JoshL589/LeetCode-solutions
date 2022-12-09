class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        max = 5000
        count = 0
        for i in weight:
            if max - i >= 0:
                count += 1
                max -= i
        return count
        