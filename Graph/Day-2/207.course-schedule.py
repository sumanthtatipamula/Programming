#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.69%)
# Total Accepted:    1.1M
# Total Submissions: 2.4M
# Testcase Example:  '2\n[[1,0]]'
#
# <p>There are a total of <code>numCourses</code> courses you have to take,
# labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an
# array <code>prerequisites</code> where <code>prerequisites[i] =
# [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you
# <strong>must</strong> take course <code>b<sub>i</sub></code> first if you
# want to take course <code>a<sub>i</sub></code>.</p>
# 
# <ul>
# <li>For example, the pair <code>[0, 1]</code>, indicates that to take course
# <code>0</code> you have to first take course <code>1</code>.</li>
# </ul>
# 
# <p>Return <code>true</code> if you can finish all courses. Otherwise, return
# <code>false</code>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
# <strong>Output:</strong> true
# <strong>Explanation:</strong> There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# </pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
# <strong>Output:</strong> false
# <strong>Explanation:</strong> There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= numCourses &lt;= 2000</code></li>
# <li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
# <li><code>prerequisites[i].length == 2</code></li>
# <li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;
# numCourses</code></li>
# <li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
# </ul>
# 
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind, adj, queue = [0] * numCourses, defaultdict(list), deque()
        for u,v in prerequisites:
            adj[v].append(u)
            ind[u] += 1
        for i in range(0, len(ind)):
            if(ind[i] == 0):
                queue.append(i)
        while(queue):
            task = queue.popleft()
            for child in adj[task]:
                ind[child] -= 1
                if(ind[child] == 0):
                    queue.append(child)
        for degree in ind:
            if(degree > 0):
                return False
        return True

        