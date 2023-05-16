class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites: 
            return [False] * numCourses

        indegree = [0] * numCourses
        graph = defaultdict(list)
        for pre in prerequisites: 
            indegree[pre[1]] += 1 
            graph[pre[0]].append(pre[1])

        queue = [i for i in range(numCourses) if indegree[i] == 0]

        lookup = {i: set() for i in range(numCourses)}
        while(queue): 
            node = queue.pop(0)
            
            for neighbour in graph[node]:
                lookup[neighbour].add(node) # add u to v 
                lookup[neighbour].update(lookup[node]) # add all pre-req of u to v 
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0: 
                    queue.append(neighbour)
        
        ans = []
        for query in queries: 
            ans.append(query[0] in lookup[query[1]])
        return ans 