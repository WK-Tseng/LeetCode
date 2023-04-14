class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for n in pushed:
            stack.append(n)
            while len(stack) > 0 and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return len(stack) == 0