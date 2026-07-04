class Solution:

    def encode(self, strs: List[str]) -> str:
        return "😀".join(strs) if len(strs) else "EMPTY_STRING"
    def decode(self, s: str) -> List[str]:
        if "EMPTY_STRING" in s:
            return []
        return s.split('😀')
