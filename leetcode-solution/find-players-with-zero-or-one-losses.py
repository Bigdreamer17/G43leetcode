class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # outdegree = defaultdict(int)
        answer = [[], []]

        for winner, loser in matches:
            graph[winner].append(loser)
        
        for vertex in graph:
            indegree[vertex] = 0

        for vertex in graph:
            for neighbour in graph[vertex]:
                indegree[neighbour] += 1

        for key in indegree.keys():
            if indegree[key] == 0:
                answer[0].append(key)
            if indegree[key] == 1:
                answer[1].append(key)
        # answer[0] = sort(answer[0])
        # answer[1] = answer[1].sort()

        sorted_ans = [sorted(sublist) for sublist in answer]
        return sorted_ans