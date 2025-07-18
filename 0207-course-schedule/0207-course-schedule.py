class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        visited = set() # track cycles
        prereq = { i:[] for i in range(numCourses) } # tracks {courses: list of prereqs (initially empty list)}

        for course, pr in prerequisites:
            prereq[course].append(pr)

        def dfs(course):

            # base cases:
            if course in visited: # cycle
                return False
            
            if prereq[course] == []: # no prereqs
                return True
            
            visited.add(course)
            
            # recursive case:
            for pr in prereq[course]: # perform dfs on each prereq
                if not dfs(pr): return False 
            
            visited.remove(course) # passed acyclic check
            prereq[course] = [] # reduce redundancy b/c already checked
            return True
        
        for course in range(numCourses): # in the case of disconnected graph
            if not dfs(course): return False
        return True