class Solution:
    def numSquares(self, n: int) -> int:
        # print(n**0.5)
        square = [i**2 for i in range(1, int(n**0.5)+1)]
        # print(square)
        
        count = 1
        queue = set([n])
        while queue:
            next_queue = set()
            for n in queue:
                for s in square:
                    temp = n - s
                    if temp == 0:
                        return count
                    elif temp > 0:
                        next_queue.add(temp)
                    else:
                        break

            count += 1
            queue = next_queue

        return 0