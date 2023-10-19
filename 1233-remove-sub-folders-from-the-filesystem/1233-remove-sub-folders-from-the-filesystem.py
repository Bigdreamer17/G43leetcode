class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False 
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.folders = [] 
        
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur  = cur.children[ch]
            
        cur.is_end = True

    def search(self):
        cur = self.root
        for key in cur.children:
            self.dfs(cur.children[key], [key])
    
    def dfs(self, cur, arr):
        if cur.is_end:
            self.folders.append(arr[:])
            return
        
        for child in cur.children:
            arr.append(child)
            self.dfs(cur.children[child], arr)
            arr.pop()
            
    def returnFolder(self):
        return self.folders 
        
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        
        for i in range(len(folder)):
            folder[i] = folder[i].split('/')
            trie.insert(folder[i])
        trie.search()
        folder = trie.returnFolder()
        
        for i in range(len(folder)):
            folder[i] = '/'.join(folder[i])
            
        return folder