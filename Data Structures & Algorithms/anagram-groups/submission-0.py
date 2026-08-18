class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count_hash = [0] * 26
            for c in s:
                count_hash[ord(c) - ord('a')] += 1
            res[tuple(count_hash)].append(s)
        return [*res.values()]