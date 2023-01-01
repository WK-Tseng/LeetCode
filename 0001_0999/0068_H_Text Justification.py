class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        temp = []
        temp_len = 0

        while len(words) > 0:
            if temp_len == 0:
                this = words.pop(0)
                temp.append(this)
                temp_len = len(this)
            else:
                this = words[0]
                if temp_len + 1 + len(this) <= maxWidth:
                    temp.append(this)
                    temp_len += 1 + len(this)
                    words.pop(0)
                else:
                    temp_list_len = len(temp)
                    if temp_list_len == 1:
                        result.append(temp[0] + ' ' * (maxWidth - temp_len))
                    else:
                        diff_len = maxWidth - temp_len
                        all_space = diff_len // (temp_list_len - 1)
                        diff_len = diff_len % (temp_list_len - 1)
                        for i in range(diff_len):
                            temp[i] += ' '
                        result.append((' '*(all_space+1)).join(temp))

                    temp.clear()
                    temp_len = 0

        last = ' '.join(temp)
        result.append(last + ' ' * (maxWidth - len(last)))

        return result