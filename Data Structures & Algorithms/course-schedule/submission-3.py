class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        lookup = defaultdict(list)
        for prereq in prerequisites:
            lookup[prereq[0]].append(prereq[1])

        def dfs(take, courses):
            for prereq in lookup[take]:
                if prereq in courses:
                    return False
                courses.add(prereq)
                if not dfs(prereq, courses):
                    return False
                courses.remove(prereq)
            lookup[take] = []
            return True
        
        taken = set()
        for courses in prerequisites:
            taken.add(courses[0])
            if not dfs(courses[0], taken):
                return False
            taken.remove(courses[0])
            lookup[courses[0]] = []

        return True