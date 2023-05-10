class Solution:
    #Function to detect cycle in an undirected graph
    def TopSort(self,node,path,parent,adj, visited):
		    visited.add(node)
    		path.add(node)
    		
    		
    		for neighbour in adj[node]:
    		    if neighbour in path and neighbour != parent:
    		        return True
    		    elif neighbour not in visited:
    		        if self.TopSort(neighbour, path, node, adj, visited):
    		            return True
    		return False
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		for node in range(V):
		    if node not in visited and self.TopSort(node ,set(), -1, adj, visited):
		        return True
		return False