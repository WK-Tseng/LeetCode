class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        charSet = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        a, b = s[:len(s)//2], s[len(s)//2:]
        count1, count2 = 0, 0
        for c1, c2 in zip(a, b):
            if c1 in charSet:
                count1 += 1
            
            if c2 in charSet:
                count2 += 1
        
        return count1 == count2