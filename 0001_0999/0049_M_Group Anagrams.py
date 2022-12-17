class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            idx = ''.join(sorted(list(s)))
            result[idx] = result.get(idx, []) + [s]
        
        return result.values()