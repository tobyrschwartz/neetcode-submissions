from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            cache[n] += 1
        for key, v in cache.items():
            buckets[v].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                res.extend(buckets[i])
            if len(res) >= k:
                return res[:k]
        return res
