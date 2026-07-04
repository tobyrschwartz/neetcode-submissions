class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        if len(s) <= 1:
            return len(s)
        left, right = 0, 1
        while left < right and right < len(s):
            sub = s[left:right+1]
            if len(set(sub)) == len(sub):
                right +=1
                max_len = max(len(sub), max_len)
            else:
                left += 1
                right += 1
        return max_len