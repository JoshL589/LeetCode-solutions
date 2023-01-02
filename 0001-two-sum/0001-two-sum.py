class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            #initialize dictionary mapping number to the index
            dic = {}

            for i in range(len(nums)):
                if target-nums[i] in dic:
                    return [dic[target-nums[i]], i]
                else:
                    dic[nums[i]] = i 