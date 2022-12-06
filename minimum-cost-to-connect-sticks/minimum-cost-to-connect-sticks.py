class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        cost = 0
        
        while len(sticks) >= 2:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            heapq.heappush(sticks, first+second)
            cost += first+second
        
        return cost