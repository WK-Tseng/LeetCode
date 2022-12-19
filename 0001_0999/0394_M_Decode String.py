class Solution:
    def decodeString(self, s: str) -> str:
        newS = []
        temp = []
        tempFlag = None
        for ss in s:
            if ss in ['[', ']']:
                if len(temp) > 0:
                    newS.append(''.join(temp))
                    temp.clear()
                    tempFlag = None
                newS.append(ss)
            else:
                if tempFlag is None:
                    if ord('a') <= ord(ss) <= ord('z'):
                        tempFlag = True
                    else:
                        tempFlag = False
                    temp.append(ss)

                elif tempFlag:
                    if ord('a') <= ord(ss) <= ord('z'):
                        temp.append(ss)
                    else:
                        newS.append(''.join(temp))
                        temp.clear()
                        tempFlag = None

                        temp.append(ss)
                else:
                    if not(ord('a') <= ord(ss) <= ord('z')):
                        temp.append(ss)
                    else:
                        newS.append(''.join(temp))
                        temp.clear()
                        tempFlag = None

                        temp.append(ss)

        if len(temp) > 0:
            newS.append(''.join(temp))
            temp.clear()
            tempFlag = None

        # print(newS)
        
        stack = []
        result = ""

        for ss in newS:
            if ss != ']':
                stack.append(ss)
            else:
                tempS = ""
                while True:
                    v = stack.pop(-1)
                    if v != '[':
                        tempS = v + tempS
                    else:
                        break
                times = int(stack.pop(-1))
                stack.append(tempS * times)

            # print(stack)

        return ''.join(stack)