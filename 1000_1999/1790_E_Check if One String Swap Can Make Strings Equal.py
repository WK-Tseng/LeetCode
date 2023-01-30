class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        diff_list = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                diff_list.append((c1, c2))
                if diff == 2:
                    if diff_list[0][0] != diff_list[1][1] or diff_list[0][1] != diff_list[1][0]:
                        return False
                elif diff > 2:
                    return False

        if diff == 1:
            return False

        return True