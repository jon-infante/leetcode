class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x,y in prerequisites:
            print(x)
            print(y)
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 1
        return True
                            
                        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(3,[[1,0], [0,1]]))