class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for node, conn in edges:
            graph[node].append(conn)
            graph[conn].append(node)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                
                dfs(nei)
        
        graph_connections = 0
        for n in range(n):
            if n not in visited:
                graph_connections += 1
                dfs(n)
        
        return graph_connections
            



            