#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#
# https://leetcode.com/problems/parallel-courses/description/
#
# algorithms
# Medium (61.78%)
# Total Accepted:    55.2K
# Total Submissions: 89.4K
# Testcase Example:  '3\n[[1,3],[2,3]]'
#
# You are given an integer n, which indicates that there are n courses labeled
# from 1 to n. You are also given an array relations where relations[i] =
# [prevCoursei, nextCoursei], representing a prerequisite relationship between
# course prevCoursei and course nextCoursei: course prevCoursei has to be taken
# before course nextCoursei.
# 
# In one semester, you can take any number of courses as long as you have taken
# all the prerequisites in the previous semester for the courses you are
# taking.
# 
# Return the minimum number of semesters needed to take all courses. If there
# is no way to take all the courses, return -1.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each
# other.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 5000
# 1 <= relations.length <= 5000
# relations[i].length == 2
# 1 <= prevCoursei, nextCoursei <= n
# prevCoursei != nextCoursei
# All the pairs [prevCoursei, nextCoursei] are unique.
# 
# 
#
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree,graph , queue, semesters= [0] * (n + 1), defaultdict(list), deque(), 0
        for u, v in relations:
            indegree[v] += 1
            graph[u].append(v)
        [queue.append(i) for i in range(n + 1) if(indegree[i] == 0)]
        while(queue):
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                for nextCourse in graph[course]:
                    indegree[nextCourse] -= 1
                    if(indegree[nextCourse] == 0):
                        queue.append(nextCourse)
        for i in range(n + 1):
            if(indegree[i] > 0):
                return -1
        return semesters
