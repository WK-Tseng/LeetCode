class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [s for s in path.split('/') if len(s) > 0 and s != '.']
        # print(path)

        stack = []
        for s in path:
            if s == '..':
                if len(stack) > 0:
                    stack.pop(-1)
            else:
                stack.append(s)

        return '/' + '/'.join(stack)