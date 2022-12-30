class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_dict = {c: i for i, c in enumerate(s)}
        
        start, end = -1, -1
        result = []

        for i, c in enumerate(s):
            if start == -1:
                start = i
                end =  end_dict[c]
            
            if i == end:
                result.append(end - start + 1)
                start, end = -1, -1
            else:
                temp_end = end_dict[c]
                if temp_end > end:
                    end = temp_end
        
        return result