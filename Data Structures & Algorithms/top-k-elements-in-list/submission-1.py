class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hash = defaultdict(int)
        for num in nums:
            num_hash[num] -= 1

        heap = []
        for num, count in num_hash.items():
            heapq.heappush(heap, (count, num))
        
        res = []
        while len(res) < k:
            count, num = heapq.heappop(heap)
            res.append(num)

        return res

        