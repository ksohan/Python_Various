class SCC:
    def dfs(self, u, visited, graph, scc):
            visited[u] = 1
            scc.append(u)
            for v in graph[u]:
                if visited[v] == 0:
                    self.dfs(v, visited, graph, scc)

    def fill_order(self, u, visited, stack, graph):
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 0:
                    self.fill_order(v, visited, stack, graph)
            stack.append(u)
            
    def transpose(self, graph, n):
        t_graph = {}
        for i in range(n):
            t_graph[i] = []
            
        for u in graph.keys():
            for v in graph[u]:
                t_graph[v].append(u)
        return t_graph

    def minimalCost(self, roads):
        n = len(roads)
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for i in range(n):
            for j in range(n):
                if roads[i][j] == 'Y':
                    graph[i].append(j)

        stack = []
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                self.fill_order(i, visited, stack, graph)
        
        visited = [0 for i in range(n)]
        t_graph = self.transpose(graph, n)
        minCost = 0
        while len(stack) > 0:
            u = stack.pop()
            if visited[u] == 0:
                
                scc = []
                self.dfs(u, visited, t_graph, scc)
                print(scc)
        
        return minCost
