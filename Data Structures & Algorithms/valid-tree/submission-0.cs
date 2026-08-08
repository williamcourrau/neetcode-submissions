public class Solution {
    public bool ValidTree(int n, int[][] edges) 
    {
        if(edges.Length != n -1){
            return false;
        }

        var map = new Dictionary<int, List<int>>();
        for(int i = 0; i < n; i++)
        {
            map[i] = new List<int>();
        }

        foreach (var edge in edges) {
            var u = edge[0];
            var v = edge[1];
            map[u].Add(v);
            map[v].Add(u);
        }

        var visited = new HashSet<int>();

        bool HasCycle(int node, int parent)
        {
            visited.Add(node);
            foreach(var n in map[node])
            {
                if(n == parent) continue;
                if(visited.Contains(n) || HasCycle(n, node))
                {
                    return true;
                }
            }

            return false;
        }

        if(HasCycle(0, -1)) return false;

        return visited.Count == n;
    }
}
