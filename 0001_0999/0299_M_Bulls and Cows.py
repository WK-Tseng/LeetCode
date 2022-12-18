class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        dict1, dict2 = {}, {}

        for n1, n2 in zip(secret, guess):
            if n1 == n2:
                A +=1
            else:
                dict1[n1] = dict1.get(n1, 0) + 1
                dict2[n2] = dict2.get(n2, 0) + 1

        for n2 in dict2:
            times = dict1.get(n2, 0)
            B += min(times, dict2[n2])

        return f'{A}A{B}B'