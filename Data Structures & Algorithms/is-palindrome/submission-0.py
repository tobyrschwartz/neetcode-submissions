class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(filter(str.isalnum, s))
        return s1.lower() == s1[::-1].lower()
        