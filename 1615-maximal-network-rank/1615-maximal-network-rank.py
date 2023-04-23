class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        
        for u,v in roads:
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        max_rank = 0
        for u in range(n):
            for v in range(u + 1, n):
                pair_rank = len(adj_list[u]) + len(adj_list[v])
                if u in adj_list[v] or v in adj_list[u]:
                    pair_rank -= 1
                max_rank = max(max_rank, pair_rank)
        
        return max_rank