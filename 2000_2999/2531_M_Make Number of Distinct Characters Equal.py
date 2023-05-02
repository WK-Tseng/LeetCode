class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        map1 = Counter(word1)
        map2 = Counter(word2)

        for c1 in counter1:

            map1[c1] -= 1
            if map1[c1] == 0:
                del map1[c1]

            map2[c1] += 1

            for c2 in counter2:
                map2[c2] -= 1
                if map2[c2] == 0:
                    del map2[c2]
                
                map1[c2] += 1

                if len(map1) == len(map2):
                    return True
                
                map2[c2] += 1
                map1[c2] -= 1
                if map1[c2] == 0:
                    del map1[c2]

            map1[c1] += 1
            map2[c1] -= 1
            if map2[c1] == 0:
                del map2[c1]

        return False