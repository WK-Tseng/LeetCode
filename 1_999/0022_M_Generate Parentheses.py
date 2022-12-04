class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ansList = []
        
        rightList = [0] * n
        
        def g(index, canRight):
            if index == n:
                if sum(rightList) == n:
                    # print(rightList)
                    s = ""
                    for i in range(n):
                        s += "("
                        s += (")" * rightList[i])
                    ansList.append(s)
                return
            
            # print(f"{index}, {canRight}")
            for i in range(0, min(index+1, canRight)+1):
                rightList[index] = i
                g(index+1, canRight + 1 - i)
        
        g(0, 1)
        return ansList