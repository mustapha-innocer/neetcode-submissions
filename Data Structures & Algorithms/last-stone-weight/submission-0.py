class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-s for s in stones]
        heapq.heapify(lst)

        while len(lst) > 1:
            x = -heapq.heappop(lst)
            y = -heapq.heappop(lst)
            if y < x:
                heapq.heappush(lst, -(x-y))
        return 0 if len(lst)==0 else -lst[0]
        