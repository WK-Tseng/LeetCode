class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        return (sy == ty and tx >= sx and (tx - sx) % sy == 0) or \
        (sx == tx and ty >= sy and (ty - sy) % sx == 0)