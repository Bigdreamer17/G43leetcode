class UnionFind:
    def __init__(self, emails):
        self.root = {email:email for email in emails}
        self.rank = {email:1 for email in emails}

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_owner = defaultdict(str)
        
        for acc in accounts:
            for i in range(1, len(acc)):
                emails_owner[acc[i]] = acc[0]
        uf = UnionFind(emails_owner)
        
        for acc in accounts:
            parent = acc[1]
            for i in range(2, len(acc)):
                uf.union(acc[i], parent)
        groups = defaultdict(list)
        
        for email in emails_owner:
            groups[uf.find(email)].append(email)
            
            
        ans = []
        for rep in groups:
            curr = [emails_owner[rep]]
            emails = groups[rep]
            emails.sort()
            
            curr.extend(emails)
            ans.append(curr)
        return ans