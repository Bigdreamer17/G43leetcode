class RandomizedSet:

    def __init__(self):
        self.hashTable = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashTable:
            return False
        
        self.hashTable[val] = len(self.arr)

        self.arr.append(val)

        return True 
    def remove(self, val: int) -> bool:
        if not val in self.hashTable:
            return False
        lst_elm = self.arr[-1]
        idx_2_rm = self.hashTable[val]

        self.hashTable[lst_elm] = idx_2_rm
        self.arr[idx_2_rm] = lst_elm

        self.arr[-1] = val

        self.arr.pop()

        self.hashTable.pop(val)
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()