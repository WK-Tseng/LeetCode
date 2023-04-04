class Solution:
    def partitionString(self, s: str) -> int:
        check = set()
        count = 0
        for c in s:
            if c not in check:
                check.add(c)
            else:
                check.clear()
                check.add(c)
                count += 1
        
        return count + 1