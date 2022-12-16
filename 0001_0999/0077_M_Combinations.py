class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        k -= 1
        result = [[i] for i in range(1, n+1)]
        
        while k > 0:
            k -= 1
            nextResult = []
            for lastResult in result:
                lastVal = lastResult[-1]
                for i in range(lastVal+1, n+1):
                    nextResult.append(lastResult + [i]) 
            result = nextResult
        
        return result