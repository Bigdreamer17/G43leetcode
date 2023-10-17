class Solution:
    def unhappyFriends(self, n: int, p: List[List[int]], pairs: List[List[int]]) -> int:
        hash_map = {}
        for pair in pairs:
            x, y = pair
            hash_map[x] = y
            hash_map[y] = x
        
        unhappy = set()
        for pref in range(n):
            for j in p[pref]:
                if hash_map[pref] == j:
                    break
                for i in p[j]:
                    if hash_map[j] == i:
                        break
                    if i == pref:   
                        unhappy.add(pref)
                        unhappy.add(j)
        return len(unhappy)
                