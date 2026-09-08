class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        cycle_start = -1
        visited = [False] * (n + 1)

        def dfs(node, parent):
            nonlocal cycle_start

            if visited[node]:
                cycle_start = node
                return True

            visited[node] = True

            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    if cycle_start != -1:
                        cycle.add(node)

                    if cycle_start == node:
                        cycle_start = -1

                    return True

            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []