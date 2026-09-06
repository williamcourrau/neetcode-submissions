class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for node, connection in edges:
            graph[node].append(connection)
            graph[connection].append(node)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return False
                
                if not dfs(nei, node):
                    return False
                
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n
