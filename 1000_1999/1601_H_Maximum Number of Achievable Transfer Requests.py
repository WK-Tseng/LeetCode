class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        requestsLen = len(requests)
        result = 0

        data = [0] * n

        def func(idx, count):
            nonlocal result

            if idx == requestsLen:
                for i in range(n):
                    if data[i] != 0:
                        return
                
                result = max(result, count)
            else:
                req = requests[idx]

                data[req[0]] -= 1
                data[req[1]] += 1
                func(idx+1, count+1)

                data[req[0]] += 1
                data[req[1]] -= 1
                func(idx+1, count)
        
        func(0, 0)
        return result