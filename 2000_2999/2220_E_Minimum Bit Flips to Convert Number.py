class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        
        max_len = max(len(start_bin), len(goal_bin))

        if len(start_bin) < max_len:
            start_bin = '0'*(max_len - len(start_bin)) + start_bin

        if len(goal_bin) < max_len:
            goal_bin = '0'*(max_len - len(goal_bin)) + goal_bin

        return sum(c1 != c2 for c1, c2 in zip(start_bin, goal_bin))
        