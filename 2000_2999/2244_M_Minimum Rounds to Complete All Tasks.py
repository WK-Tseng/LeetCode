class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        '''
        1 % 3 = 1 : X
        2 % 3 = 2 : O -> 1
        3 % 3 = 0 : O -> 1

        4 % 3 = 1 : O -> 2
        5 % 3 = 2 : O -> 2
        6 % 3 = 0 : O -> 2

        7 % 3 = 1 : O -> 3
        8 % 3 = 2 : O -> 3
        9 % 3 = 0 : O -> 3

        10 % 3 = 1 : O -> 4
        '''
        min_count = 0
        for times in Counter(tasks).values():
            if times == 1:
                return -1
            min_count += (times + 2) // 3
        return min_count