class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sub_dict = {}
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            sub_dict[sub] = sub_dict.get(sub, 0) + 1
        
        return [sub for sub, times in sub_dict.items() if times > 1]