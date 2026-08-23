class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prerequisites = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_to_prerequisites[course].append(prerequisite)

        course_order = []
        fully_resolved = set()
        courses_in_current_path = set()

        def dfs(course):
            if course in courses_in_current_path:
                return False
            if course in fully_resolved:
                return True

            courses_in_current_path.add(course)
            for prerequisite in course_to_prerequisites[course]:
                if dfs(prerequisite) == False:
                    return False
            courses_in_current_path.remove(course)
            fully_resolved.add(course)
            course_order.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return course_order


"""This is the same directed-graph cycle question as Course Schedule I, but now I also need to produce a valid order, not just say yes/no — so I'll run the same path-tracking DFS for cycle detection, but additionally append each course to an output list right after all of its prerequisites have been fully resolved, which naturally builds a valid topological order since a course can only be appended once everything it depends on is already in the list. I need two separate sets rather than one: one tracking courses currently on the active DFS path (to catch cycles), and one tracking courses that are fully done and safe to short-circuit on future visits (to avoid redundant re-exploration and, critically, to avoid mistaking 'already fully processed, totally fine' for 'currently mid-cycle'), whereas Course Schedule I could get away with mutating the prerequisite map itself as a cheaper memoization trick since it didn't need to preserve order information afterward. I chose this DFS-with-two-sets approach over Kahn's algorithm (BFS processing zero-in-degree nodes, decrementing in-degrees as courses complete) as the natural alternative — Kahn's is arguably more intuitive for producing a topological order directly and avoids recursion depth concerns on deep graphs, but I'm sticking with DFS here since it directly extends the cycle-detection logic I already have, trading Kahn's flatter iterative bookkeeping for DFS's more direct reuse of path-tracking I've already built. This runs in O(V + E) time, since each course and prerequisite edge is processed a constant number of times across all DFS calls, and O(V + E) space for the adjacency map, the output list, and the two tracking sets plus recursion stack in the worst case."""