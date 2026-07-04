class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        l = len(heights)
        left, right = 0, l - 1
        while left < right:
            amt = (right - left) * (min(heights[left], heights[right]))
            max_amt = max(max_amt, amt)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_amt