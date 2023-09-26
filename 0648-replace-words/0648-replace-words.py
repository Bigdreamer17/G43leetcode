class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        parent = self.root
        for c in word:
            if not c in parent.children:
                parent.children[c] = TrieNode()
            parent = parent.children[c]
        parent.is_end = True
        
    def search(self, word):
        parent = self.root
        ans = ''
        for c in word:
            if not c in parent.children:
                return word
            ans += c
            parent = parent.children[c]
            if parent.is_end == True:
                return ans
        return word
    
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        sent = sentence.split()
        ans = []
        
        for word in sent:
            ans.append(trie.search(word))
            
        return " ".join(ans)