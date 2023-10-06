class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch] 
        root.end = True
        root.count += 1
            
    

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        root = trie.root
        
        for word in words:
            trie.insert(word)
            
        
        def find_idx(ch, i):
            
            for j in range(i, len(s)):
                if s[j] == ch:
                    return j
            return -1
            
        def solve(node, last_idx):
            nonlocal ans
            if node.end:
                ans += node.count
                
            for ch in node.children:
                idx = find_idx(ch, last_idx + 1)
                if idx != -1:
                    solve(node.children[ch], idx)
            return
            
            
        ans = 0
        solve(root, -1)
        return ans