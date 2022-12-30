class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        pattern_dict = {}
        s_set = set()

        if len(s_list) != len(pattern):
            return False

        for p, s in zip(pattern, s_list):
            if p not in pattern_dict:
                pattern_dict[p] = s

                if s not in s_set:
                    s_set.add(s)
                else:
                    return False
            else:
                if pattern_dict[p] != s:
                    return False
        
        return True