class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
                
        def try_split_ip(i, s, split_list, results):
            s_len = len(s)
            if i == 4:
                if s_len == 0:
                    # print(split_list)
                    results.append(list(split_list))
                return
            elif s_len > 3 * (4-i):
                return
            
            for j in range(min(3, s_len)):
                temp = s[:j+1]
                if temp.isdigit() and 0 <= int(s[:j+1]) <= 255 and str(int(s[:j+1])) == temp:
                    split_list.append(temp)
                    try_split_ip(i+1, s[j+1:], split_list, results)
                    split_list.pop(-1)
        
        results = []
        try_split_ip(0, s, [], results)

        return ['.'.join(result) for result in results]