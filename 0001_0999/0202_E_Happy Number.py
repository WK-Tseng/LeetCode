class Solution:
    def isHappy(self, n: int) -> bool:
        total = n
        record = set()

        while total != 1 and total not in record:
            record.add(total)
            temp = 0
            for c in str(total):
                temp += int(c)**2
            total = temp
            
        return total == 1