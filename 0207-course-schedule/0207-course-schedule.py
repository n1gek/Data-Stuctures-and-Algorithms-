from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        schedule = defaultdict(list)

        for preq in prerequisites:
            a, b = preq
            schedule[a].append(b)
        
        visited = set() # this marks the visited courses
        
        # the helper will work on one course at a time
        def helper(course):
            if course in visited:  
                return False
            
            if schedule[course] == []: # if a course doesnt have prereqs, then return True
                return True
            
            visited.add(course)    # now perfoem depth first on the course
            for preq in schedule[course]:
                if not helper(preq):
                    return False
            
            visited.remove(course)
            schedule[course] = [] # this will help us narrow down the search
            return True
        
        for i in range(numCourses):
            if not helper(i):
                return False
        
        return True

        



        


        