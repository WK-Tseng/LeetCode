class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 1
        # 3, 2
        # 4, 5, 6, 7
        # 15, 14, 13, 12, 11, 10, 9, 8

        # 1
        # 11, 10
        # 100, 101, 110, 111
        # 1111, 1110, 1101, 1100, 1011, 1010, 1001, 1000

        result = [label]
        while (label > 1):
            label >>= 1
            label ^= (1 << (label.bit_length()-1)) - 1
            result.append(label)

        return result[::-1]