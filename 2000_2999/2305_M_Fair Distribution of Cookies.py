class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        result = float('inf')
        data = [0] * k

        def fun(idx):
            nonlocal result

            maxData = max(data)

            if idx == n:
                result = min(result, maxData)
                return
            
            if result <= maxData:
                return

            for i in range(k):
                data[i] += cookies[idx]
                fun(idx + 1)
                data[i] -= cookies[idx]
            
        fun(0)

        return result