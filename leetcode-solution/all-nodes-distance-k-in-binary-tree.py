# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildGraph(self, root, parent, graph):
        if root:
            if parent:
                graph[root].append(parent)
                graph[parent].append(root)

            self.buildGraph(root.left, root, graph)
            self.buildGraph(root.right, root, graph)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)

        # BFS
        visited = set()
        queue = deque([(target, 0)])
        answer = []

        while queue:
            current, distance = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            if distance == k:
                answer.append(current.val)
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

        return answer