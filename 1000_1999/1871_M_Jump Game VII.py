class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # queue = [0]
        queue = collections.deque([0])
        maxIdx = 0

        while queue:
            # idx = queue.pop(0)
            idx = queue.popleft()
            if idx == n-1:
                return True
            
            start = max(idx+minJump, maxIdx+1)
            for i in range(start, min(idx+maxJump+1, n)):
                if s[i] == '0':
                    queue.append(i)

            maxIdx = idx+maxJump

        return False