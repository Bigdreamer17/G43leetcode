class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        parent = self.root
        for c in word:
            if not c in parent.child:
                parent.child[c] = TrieNode()
            parent = parent.child[c]
        parent.end = True

    def search(self, word):
        parent = self.root
        ans = ''
        for c in word:
            if not c in parent.child:
                return word
            ans += c
            parent = parent.child[c]
            if parent.end == True:
                return ans
        return word
            
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        graph = Trie()
        list_word = sentence.split()
        for dic in dictionary:
            graph.insert(dic)
        ans = []
        for word in list_word:
            ans.append(graph.search(word))
        
        return " ".join(ans)









# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         cur = self.root
        
#         for wd in word:
#             index = ord(wd) - ord('a')
#             if cur.children[index] is None:
#                 cur.children[index] = TrieNode()
                
#             cur = cur.children[index]
#         cur.is_end = True
        
#     def startwith(self, prefix: str) -> bool:
#         cur = self.root
#         for ch in word:
#             indx = ord(ch) - ord('a')
#             if cur.children[indx] is None:
#                 return False

#             cur = cur.children[indx]
#         return True
    
# class TrieNode:
#     def __init__(self):
#         self.is_end = False
#         self.children = [ None for _ in range(26)]

# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         trie = Trie()
        
#         for word in dictionary:
#             trie.insert(word)
        
#         sen = sentence.split()
    
#         for indx, sent in enumerate(sen):
#             if trie.startwith(sent):
#                 sen[indx] = 