class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        number_of_pieces = k + 1
        l = min(sweetness)
        r = sum(sweetness) // (k+1)
        def check(sweet):
            count = 0
            cur_sweetness = 0
            for i in sweetness:
                cur_sweetness += i
                if cur_sweetness >= sweet:
                    count += 1
                    cur_sweetness = 0
            return count >= k+1

        while l < r:
            sweet = (l+r+1)//2
            if check(sweet):
                l = sweet
            else:
                r = sweet -1
        
        return r
