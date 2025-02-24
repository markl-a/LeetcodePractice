from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        parent = [-1] * n
        queue = deque([0])
        parent[0] = -1
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if parent[v] == -1 and v != parent[u]:
                    parent[v] = u
                    queue.append(v)
        
        bob_path = []
        current = bob
        while current != -1:
            bob_path.append(current)
            current = parent[current]
        
        bob_time = [float('inf')] * n
        time = 0
        for node in bob_path:
            if time < bob_time[node]:
                bob_time[node] = time
                time += 1
        

        max_score = -float('inf')
        
        def dfs(u, parent_u, t, score):
            nonlocal max_score
            # 计算当前节点的得分
            if t < bob_time[u]:
                add = amount[u]
            elif t == bob_time[u]:
                add = amount[u] // 2
            else:
                add = 0
            new_score = score + add
            
            is_leaf = True
            for v in adj[u]:
                if v != parent_u:
                    is_leaf = False
                    dfs(v, u, t + 1, new_score)
            
            if is_leaf:
                if new_score > max_score:
                    max_score = new_score
        
        dfs(0, -1, 0, 0)
        return max_score