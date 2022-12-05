class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        
        midIdx = len(nums1) + len(nums2)
        evenFlag = False
        
        if midIdx % 2 == 0:
            evenFlag = True
            midIdx = midIdx//2
        else:
            midIdx = (midIdx+1)//2
            
        Idx1 = 0
        Idx2 = 0
        
        andNum = 0
        
        while True:
            temp = 0
            
            if Idx1 < nums1Len and Idx2 < nums2Len:
                if nums1[Idx1] <= nums2[Idx2]:
                    temp = nums1[Idx1]
                    Idx1 += 1
                else:
                    temp = nums2[Idx2]
                    Idx2 += 1
            elif Idx1 < nums1Len:
                temp = nums1[Idx1]
                Idx1 += 1
            elif Idx2 < nums2Len:
                temp = nums2[Idx2]
                Idx2 += 1
                
            midIdx -= 1
            
            if midIdx == 0:
                if andNum != 0:
                    andNum += temp         
                    andNum /= 2.0
                else:
                    andNum += temp 
                
                if evenFlag:
                    midIdx += 1
                    evenFlag = False
                else:
                    return andNum
            