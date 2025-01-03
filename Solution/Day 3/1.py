#approach 
# find a possibles distances and do bfs

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i , ( x1 , y1 , r1) in enumerate(bombs):
            for j , ( x2 , y2 , r2) in enumerate(bombs):
                if i != j:
                    dist = sqrt((x2-x1)**2 + (y2-y1)**2)
                    if dist <= r1:
                        graph[i].append(j)

        def dfs(node , visited):
            visited.add(node)
            cnt = 1
            for child in graph[node]:
                if child not in visited:
                    cnt += dfs(child,visited )
            return cnt
        
        res = 0
        print(graph)

        for i in range(len(bombs)):
            res = max(res , dfs(i , set()))

        return res
