class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            indx = ord(ch) - ord('a')
            if cur.children[indx] is None:
                cur.children[indx] = TrieNode()
            
            cur = cur.children[indx]
        cur.is_end =True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            indx = ord(ch) - ord('a')
            if cur.children[indx] is None:
                return False
            
            cur = cur.children[indx]
        if cur.is_end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            indx = ord(ch) - ord('a')
            if cur.children[indx] is None:
                return False
            
            cur = cur.children[indx]
        return True
        
class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26)]
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)