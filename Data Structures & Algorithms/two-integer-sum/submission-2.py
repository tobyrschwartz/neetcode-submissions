class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i in range(len(nums)):
            j = nums[i]
            s = target - j
            if cache.get(s, -1) != -1:
                n = cache.get(s)
                return [n, i]
            cache[nums[i]] = i

        