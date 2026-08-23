class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its list of prerequisite courses
        course_to_prerequisites = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_to_prerequisites[course].append(prerequisite)

        # Tracks all courses along the current DFS path (for cycle detection)
        courses_in_current_path = set()

        def dfs(course):
            if course in courses_in_current_path:
                # Cycle detected
                return False
            if course_to_prerequisites[course] == []:
                return True

            courses_in_current_path.add(course)
            for prerequisite in course_to_prerequisites[course]:
                if not dfs(prerequisite):
                    return False
            courses_in_current_path.remove(course)
            course_to_prerequisites[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


"""Since 'must take b before a' naturally forms a directed edge from a to b, the whole question of whether all courses can be finished collapses into asking whether this directed graph has a cycle — if there's a cycle, some set of courses depends on each other in a loop with no valid starting point, so it's impossible. I'll build an adjacency map from each course to its prerequisites, then run DFS from every course, tracking the set of courses currently 'in progress' along the current path — if DFS ever revisits a course still in that in-progress set, that's a cycle, so I return false; if a course has no prerequisites left to explore, it's safely completable. Once a course is confirmed cycle-free, I clear its prerequisite list so future DFS calls skip re-exploring it, effectively memoizing completed subgraphs. I chose DFS with a 'currently in path' set over BFS or a plain visited-forever set because cycle detection in a directed graph specifically needs to distinguish 'visited on this path' from 'visited and fully resolved,' which a single global visited set can't do, and DFS naturally lets me track and unwind that path via the call stack — I also chose this DFS approach over Kahn's algorithm (BFS with in-degree counting) as an alternative worth naming, trading Kahn's more mechanical 'process zero-in-degree nodes' bookkeeping for DFS's more direct 'walk the dependency chain and catch revisits' logic, though both give the same complexity. This runs in O(V + E) time, since each course and each prerequisite edge is processed a constant number of times across all DFS calls combined, and O(V + E) space for the adjacency map plus the recursion stack and path-tracking set in the worst case."""