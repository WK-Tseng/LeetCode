class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 1
        left, right = 0, 0
        fruits_dict = Counter()
        fruits_dict[fruits[0]] += 1

        for fruit in fruits[1:]:
            if fruit not in fruits_dict:
                while len(fruits_dict) >= 2:
                    temp = fruits[left]
                    while fruits[left] == temp:
                        left += 1
                        fruits_dict[temp] -= 1
                        if fruits_dict[temp] == 0:
                            fruits_dict.pop(temp)
            
            right += 1
            fruits_dict[fruit] += 1
            max_len = max(max_len, right - left + 1)
                    
        return max_len