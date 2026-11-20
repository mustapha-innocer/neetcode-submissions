class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        hp = []
        heapq.heapify(hp)
        for num, cnt in counts.items():
            heapq.heappush(hp, (cnt,num))
            if len(hp) > k:
                heapq.heappop(hp)
        return [v[1] for v in hp]


        