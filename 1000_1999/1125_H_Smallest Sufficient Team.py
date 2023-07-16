class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillLen = len(req_skills)
        skillIdx = {skill:i for i, skill in enumerate(req_skills)}
        dp = {0: []}

        for i, peopleSkill in enumerate(people):
            skillBit = 0
            for skill in peopleSkill:
                skillBit |= 1 << skillIdx[skill]

            for tBit, peopleList in dict(dp).items():
                newSkillBit = tBit | skillBit
                if newSkillBit != tBit:
                    if (newSkillBit not in dp) or len(dp[newSkillBit]) > len(peopleList) + 1:
                        dp[newSkillBit] = peopleList + [i]

        return dp[(1 << skillLen)-1]