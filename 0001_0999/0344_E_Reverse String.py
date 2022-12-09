class Solution:
    # AC
    # def reverseString(self, s: List[str]) -> None:
    #     start, end = 0, len(s) - 1
    #     while start < end:
    #         s[start], s[end] = s[end], s[start]
    #         start += 1
    #         end -= 1

    # AC
    # def reverseString(self, s: List[str]) -> None:
    #     for i in range(len(s)//2):
    #         s[i], s[-(i+1)] = s[-(i+1)], s[i]

    # AC, fast
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]