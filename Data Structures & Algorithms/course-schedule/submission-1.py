class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # do cycles mean that we cannot meet prerequisites? yes
        # is it safe to assume all inputs are valid? yes
        
        # input: number of courses (int), 2D matrix where each array [a, b] means you need to take b before a
        # output: boolean
        # goal: find out if it is possible to take all the courses

        # initial approach:
        # create a hash map with courses and their prereq
        preMap = { i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        visitSet = set()
        # dfs helper function
        def dfs(course: int) -> bool:
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        # iterate through prerequisites [a, b]
        for course in range(numCourses):
            if not dfs(course):
                return False
            # run dfs on b with path
        return True
        