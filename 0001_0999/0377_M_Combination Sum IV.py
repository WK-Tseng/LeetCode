class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        amount = target
        coins = sorted(nums)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for target in range(amount + 1):
            for coin in coins:
                if coin > target:
                    break
                elif coin == target:
                    dp[target] += 1
                else:
                    dp[target] += dp[target - coin]

        return dp[amount]

    # timeout
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     amount = target
    #     coins = nums

    #     dp = [[0, None] for _ in range(amount + 1)]
    #     dp[0][0] = 1
    #     dp[0][1] = [Counter()]

    #     for coin in coins:
    #         for target in range(coin, amount + 1):
    #             if dp[target - coin][0] == 0:
    #                 pass
    #             else:
    #                 dp[target][0] += dp[target - coin][0]
                    
    #                 temp = []
    #                 for counter in dp[target - coin][1]:
    #                     temp.append(Counter(counter))
    #                     temp[-1][coin] += 1

    #                 if dp[target][1]:
    #                     dp[target][1] += temp
    #                 else:
    #                     dp[target][1] = temp

    #         # print('------', coin)
    #         # for d in dp:
    #         #     print(d)

    #     factorial_list = [0, 1]
    #     def factorial(n):
    #         if n < len(factorial_list):
    #             return factorial_list[n]
            
    #         this_n = len(factorial_list) - 1
    #         while n != this_n:
    #             this_n += 1
    #             factorial_list.append(factorial_list[-1] * this_n)

    #         return factorial_list[n]

    #     if dp[amount][1]:
    #         count = 0
    #         for counter in dp[amount][1]:
    #             # print(d)
    #             total = 0
    #             c = 1
    #             for coin in counter:
    #                 total += counter[coin]
    #                 c *= factorial(counter[coin])
    #             count += factorial(total) // c
    #         return count
    #     else:
    #         return 0
