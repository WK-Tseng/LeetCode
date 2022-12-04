# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
            head = None
            nowNode = None

            while (list1 != None) or (list2 != None):
                # temp1 = list1
                # temp2 = list2

                flag = 0

                if (list1 != None) and (list2 != None):
                    if list1.val <= list2.val:
                        flag = 1
                    else:
                        flag = 2
                else:
                    if list1 != None:
                        flag = 1
                    else:
                        flag = 2

                if flag == 1:
                    if head is None:
                        head = list1
                        nowNode = head
                    else:
                        nowNode.next = list1
                        nowNode = nowNode.next
                    list1 = list1.next
                else:
                    if head is None:
                        head = list2
                        nowNode = head
                    else:
                        nowNode.next = list2
                        nowNode = nowNode.next
                    list2 = list2.next

                # print("-----------")
                # print(head)
                # print(list1)
                # print(list2)

            return head
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        
        tempLists = lists
        flag = False
        while not flag:
            tempLists_2 = []
            idx = 0
            for i in range(0, len(tempLists), 2):
                if i+1 == len(tempLists):
                    tempLists_2.append(tempLists[i])
                else:
                    tempLists_2.append(mergeTwoLists(tempLists[i], tempLists[i+1]))
                idx += 1
            
            tempLists = tempLists_2
            
            if idx == 1:
                flag = True
        
        return tempLists[0]