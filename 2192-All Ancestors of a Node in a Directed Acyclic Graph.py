class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        dict_child = defaultdict(list)
        ancestor = [[] for _ in range(n)]
        for edge in edges:
            dict_child[edge[0]].append(edge[1])
        def dfs(pre, cur):
            for child in dict_child[cur]:
                if ancestor[child] != [] and ancestor[child][-1] == pre:
                    continue
                ancestor[child].append(pre)
                dfs(pre, child)
        for i in range(n):
            dfs(i, i)
        return ancestor