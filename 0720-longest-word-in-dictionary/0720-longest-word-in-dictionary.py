class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        curWord = []
        
        for w in word:
            curWord.append(w)
            if w not in cur.children:  
                if len(curWord) == len(word):
                    cur.children[w] = TrieNode()
                    return "".join(curWord)
                return ""

            cur = cur.children[w]
        
        return ""
                

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longestWord = ""
        largestLeng = 0
        words.sort()
        
        for word in words:
            curword = trie.insert(word)
            if len(curword) > largestLeng:
                longestWord = curword
                largestLeng = len(curword)
            if len(curword) == largestLeng:
                longestWord = min(longestWord, curword)
        return longestWord
                