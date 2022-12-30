# AC, implement
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print(self):
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        print(result)

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        result = -1
        if index < self.len:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            result = temp_node.val
        return result

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        self.len += 1

        if self.len == 1:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.len += 1
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.len:
            if index == 0:
                self.addAtHead(val)
            elif index == self.len:
                self.addAtTail(val)
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next
                
                new_node = Node(val, self.head)
                temp_node_next = temp_node.next
                temp_node.next = new_node
                new_node.next = temp_node_next

                self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < self.len:
            if index == 0:
                self.head = self.head.next
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next

                temp_node_next = temp_node.next
                if temp_node_next:
                    temp_node.next = temp_node.next.next
                else:
                    temp_node.next = None

                if temp_node_next == self.tail:
                    self.tail = temp_node

            self.len -= 1


# AC, but use built-in List
# class MyLinkedList:

#     def __init__(self):
#         self.data = []

#     def get(self, index: int) -> int:
#         try:
#             return self.data[index]
#         except:
#             return -1

#     def addAtHead(self, val: int) -> None:
#         self.data.insert(0, val)

#     def addAtTail(self, val: int) -> None:
#         self.data.append(val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index <= len(self.data):
#             self.data.insert(index, val)

#     def deleteAtIndex(self, index: int) -> None:
#         try:
#             self.data.pop(index)
#         except:
#             pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)