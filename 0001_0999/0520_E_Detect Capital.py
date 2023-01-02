class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = [s.islower() for s in word]
        return all(flag) or all((not f) for f in flag) or ((not flag[0]) and all(flag[1:] or [True]))