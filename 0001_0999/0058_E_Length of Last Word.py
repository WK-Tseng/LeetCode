class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for ss in s.split(' ')[::-1]:
            if len(ss) != 0:
                return len(ss)
                
        return 0