class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        l = len(nums)
        for i in range(0, l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            j, k = i + 1, l - 1
            while j < k and j < l:
                s = nums[i] + nums[j] + nums[k] 
                if s > 0:
                    k -= 1
                if s < 0:
                    j += 1
                if s == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
        return triplets
