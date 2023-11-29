class MagicDictionary:

    def __init__(self):
        self.table = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            if len(d) not in self.table:
                self.table[len(d)]
            
            self.table[len(d)].append(d)

    def offbyone(self, searchword, word):
        diff = 0
        for i in range(len(word)):
            if word[i] != searchword[i]:
                diff += 1
        if diff != 1:
            return False
        else:
            return True
    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.table:
            return False
        match = self.table[len(searchWord)]
        for m in match:
            if self.offbyone(searchWord, m):
                return True 
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)