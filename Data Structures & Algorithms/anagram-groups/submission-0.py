class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict()
        answers = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort in cache:
                i = cache[sort]
                answers[i].append(s)
            else:
                cache[sort] = len(answers)
                answers.append([s])
        return answers