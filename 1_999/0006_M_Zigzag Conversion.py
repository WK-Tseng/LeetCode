class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = (numRows + (numRows-2)) if numRows >= 3 else numRows
        
        initStep = step
        initLen = len(s)
        
        ansStr = ""
        ansLen = 0
        
        Idx = 0
        
        while ansLen != initLen:
            #ansStr += s[Idx::step]
            thisIdx = Idx
            thisStep = step
            while thisIdx < initLen:
                ansStr += s[thisIdx]
                ansLen += 1
                thisIdx += thisStep
                thisStep = initStep - thisStep
                if thisStep == 0:
                    thisStep = initStep
            
            
            #ansLen = len(ansStr)
            
            Idx += 1
            step -= 2
            if step == 0:
                step = initStep
                
        return ansStr