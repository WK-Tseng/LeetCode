class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = (tomatoSlices // 2 - cheeseSlices) 
        small = cheeseSlices - jumbo

        if jumbo < 0 or small < 0:
            return []
        if jumbo * 4 + small * 2 != tomatoSlices:
            return []

        return [jumbo, small]