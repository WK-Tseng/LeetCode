class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = [0, 1, 1]

        if n < 3:
            return sequence[n]
        else:
            sum_sequence = 1
            for _ in range(n-2):
                sum_sequence += sequence[-1]
                sequence.append(sum_sequence)
                sum_sequence -= sequence.pop(0)

            return sequence[-1]