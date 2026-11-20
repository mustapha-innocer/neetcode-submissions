class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        hp = [(-v, k) for k, v in counts.items()]
        heapq.heapify(hp)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(hp)[1])
        return ans


        