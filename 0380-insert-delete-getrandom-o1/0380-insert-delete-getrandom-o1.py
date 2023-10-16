class RandomizedSet:

    def __init__(self):
        self.RandSet = set()
    def insert(self, val: int) -> bool:
        if val not in self.RandSet:
            self.RandSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.RandSet:
            self.RandSet.remove(val)
            return True 
        else:
            return False

    def getRandom(self) -> int:
        new_list = list(self.RandSet)
        Random_value = random.choice(new_list)
        return Random_value


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()