class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_counter = Counter(num)

        result = ''

        for i in range(9, 0, -1):
            if num_counter[str(i)] >= 2:
                result += str(i) * (num_counter[str(i)] // 2)
                num_counter[str(i)] %= 2
        
        if result and num_counter['0']:
            result += '0' * (num_counter['0'] // 2)
            num_counter['0'] %= 2

        for i in range(9, -1, -1):
            if num_counter[str(i)]:
                return result + str(i) + result[::-1]
        
        return result + result[::-1]

    # AC, slow
    # def largestPalindromic(self, num: str) -> str:
    #     num_counter = Counter([int(n) for n in num])
    #     # print(num_counter)

    #     result = []

    #     temp = []
    #     for i in range(10):
    #         if num_counter[i] % 2 == 1:
    #             temp.append(i)

    #     if temp:
    #         i = max(temp)
    #         result.append(str(i))
    #         num_counter[i] -= 1

    #     exit_flag = False
    #     while not exit_flag:
    #         exit_flag = True
    #         for i in range(10):
    #             if num_counter[i] >= 2:
    #                 result.insert(0, str(i))
    #                 result.append(str(i))
    #                 num_counter[i] -= 2
    #                 exit_flag = False
    #                 break

    #     # print(result)
    #     # print(''.join(result))

    #     while len(result) > 1 and result[0] == '0':
    #         result.pop(0)
    #         result.pop(-1)

    #     if len(result) == 0:
    #         result.append('0')

    #     return ''.join(result)