class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        adj = defaultdict(list)
        for v, u in enumerate(parent):
            adj[u].append(v)
        def dfs(source):
            total_val = value[source]
            total_elements = 1
            for child in adj[source]:
                val, elements = dfs(child)
                total_val += val
                total_elements += elements
            if(total_val == 0):
                return [0, 0]
            return [total_val, total_elements]
        return dfs(0)[-1]