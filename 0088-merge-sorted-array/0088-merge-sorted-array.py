class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #two pointers, filling the array starting from the end
        
        l = m - 1
        r = n - 1
        x = m + n - 1

        
        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[x] = nums1[l]
                x -= 1
                l -= 1
            else:
                nums1[x] = nums2[r]
                x -= 1
                r -= 1

        while r >= 0:   
            nums1[x] = nums2[r]
            x -= 1
            r -= 1