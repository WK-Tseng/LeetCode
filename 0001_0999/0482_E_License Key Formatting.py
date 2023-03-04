class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.upper().split('-'))
        s_len = len(s)
        result_list = []
        if s_len % k != 0:
            result_list.append(s[:s_len % k])
            s = s[s_len % k:]

        # for i in range(s_len // k):
        #     result_list.append(s[i*k:(i+1)*k])
        result_list += [s[i*k:(i+1)*k] for i in range(s_len // k)]

        return '-'.join(result_list)