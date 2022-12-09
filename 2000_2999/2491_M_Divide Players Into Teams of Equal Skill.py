class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sumSkill = sum(skill)
        teamSkill = sumSkill // (len(skill) // 2)
        skillDict = {}
        result = 0
        for s in skill:
            if s in skillDict:
                skillDict[s] -= 1
                if skillDict[s] == 0:
                    del skillDict[s]
                result += s * (teamSkill - s)
            else:
                skillDict[teamSkill - s] = skillDict.get(teamSkill - s, 0) + 1

        return result if len(skillDict) == 0 else -1