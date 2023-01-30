class MyLinkedList:

    def __init__(self):
        self.values = []

    def get(self, index: int) -> int:
        if index < len(self.values):
            return self.values[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.values.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.values.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.values):
            return
        elif index == len(self.values):
            self.values.append(val)
        else:
            self.values.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.values):
            self.values.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)