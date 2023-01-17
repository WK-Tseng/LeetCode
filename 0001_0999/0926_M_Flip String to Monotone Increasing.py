class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        flip_0, flip_1 = [0]*N, [0]*N
        count_0, count_1 = 0, 0

        for i in range(N):
            if s[i] == '1':
                count_0 += 1
            flip_0[i] = count_0
            
            if s[-(i+1)] == '0':
                count_1 += 1
            flip_1[-(i+1)] = count_1

        # print(flip_0)
        # print(flip_1)

        flip_0.insert(0, 0)
        flip_1.append(0)

        result = N
        for i in range(N+1):
            result = min(result, flip_0[i] + flip_1[i])

        return result