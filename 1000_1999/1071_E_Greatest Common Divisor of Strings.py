class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = lambda a, b: (a if b == 0 else gcd(b, a % b))
        return "" if str1+str2 != str2+str1 else str1[0: gcd(len(str1), len(str2))]