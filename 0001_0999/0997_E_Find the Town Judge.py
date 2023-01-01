class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust1_dict = {(i+1): 0 for i in range(n)}
        trust2_dict = {(i+1): 0 for i in range(n)}

        for p1, p2 in trust:
            trust1_dict[p2] += 1
            trust2_dict[p1] += 1

        for p in trust1_dict:
            if trust1_dict[p] == n - 1 and trust2_dict[p] == 0:
                return p
        
        return -1
