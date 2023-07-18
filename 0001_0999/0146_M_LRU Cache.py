class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def printValue(self):
        s = ''
        n = self
        while n:
            s +=  '[' + str(n.key) + ', ' + str(n.value) + '], '
            n = n.next
        print(s)

class LRUCache:

    def __init__(self, capacity: int):
        self.cacheDict = {}
        self.linkList = None
        self.lastNode = None
        self.limit = capacity

        # print('---------')

    def get(self, key: int) -> int:
        if key in self.cacheDict:
            node = self.cacheDict[key]

            if self.linkList != self.lastNode:

                if node == self.linkList:
                    self.linkList = self.linkList.next
                    self.linkList.prev = None

                    node.next = None
                    if self.lastNode:
                        self.lastNode.next = node
                    node.prev = self.lastNode
                    self.lastNode = node

                elif node == self.lastNode:
                    pass
                else:
                    prevNode, nextNode = node.prev, node.next
                    if prevNode:
                        prevNode.next = nextNode
                    else:
                        self.linkList = nextNode

                    if nextNode:
                        nextNode.prev = prevNode

                    node.next = None
                    if self.lastNode:
                        self.lastNode.next = node
                    node.prev = self.lastNode
                    self.lastNode = node

            # self.linkList.printValue()

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            node = self.cacheDict[key]
            node.value = value

            if self.linkList != self.lastNode:

                if node == self.linkList:
                    self.linkList = self.linkList.next
                    self.linkList.prev = None

                    node.next = None
                    if self.lastNode:
                        self.lastNode.next = node
                    node.prev = self.lastNode
                    self.lastNode = node

                elif node == self.lastNode:
                    pass
                else:
                    prevNode, nextNode = node.prev, node.next
                    if prevNode:
                        prevNode.next = nextNode
                    else:
                        self.linkList = nextNode

                    if nextNode:
                        nextNode.prev = prevNode

                    node.next = None
                    if self.lastNode:
                        self.lastNode.next = node
                    node.prev = self.lastNode
                    self.lastNode = node

        else:
            node = Node(key, value)
            if self.lastNode:
                self.lastNode.next = node
            else:
                self.linkList = node

            node.prev = self.lastNode
            self.lastNode = node

            self.cacheDict[key] = node

            if len(self.cacheDict) > self.limit:
                delNode = self.linkList
                self.cacheDict.pop(delNode.key)

                self.linkList = self.linkList.next
                self.linkList.prev = None

        # self.linkList.printValue()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)