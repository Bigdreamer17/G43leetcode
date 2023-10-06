class Solution:
    def removeDuplicates(self, s: str) -> str:
        store = deque()
        
        for ch in s:
            if store and store[-1] == ch:
                store.pop()
            else:
                store.append(ch)
        return "".join(store)