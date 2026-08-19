class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hash = defaultdict(int)
        for num in nums:
            num_hash[num] += 1

        ls = []
        for key, val in num_hash.items():
            ls.append((key, val))

        ls.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(ls[i][0])

        return res