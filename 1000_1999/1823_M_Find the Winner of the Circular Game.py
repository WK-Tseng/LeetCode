class Solution:
    # AC, fast
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i+1 for i in range(n)]
        index = 0
        k -= 1

        while len(circle) > 1:
            index += k
            index %= len(circle)
            circle.pop(index)

        return circle[0]


    
    # AC, slow
    # def findTheWinner(self, n: int, k: int) -> int:
    #     circle = [i+1 for i in range(n)]

    #     while len(circle) > 1:
    #         for _ in range(k):
    #             circle.append(circle.pop(0))
    #         circle.pop(-1)

    #     return circle[0]