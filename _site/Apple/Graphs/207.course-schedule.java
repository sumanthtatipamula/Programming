package Apple.Graphs;

import java.util.*;

/*
 * @lc app=leetcode id=207 lang=java
 *
 * [207] Course Schedule
 *
 * https://leetcode.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (44.69%)
 * Likes:    12034
 * Dislikes: 471
 * Total Accepted:    1.1M
 * Total Submissions: 2.4M
 * Testcase Example:  '2\n[[1,0]]'
 *
 * There are a total of numCourses courses you have to take, labeled from 0 to
 * numCourses - 1. You are given an array prerequisites where prerequisites[i]
 * = [ai, bi] indicates that you must take course bi first if you want to take
 * course ai.
 *
 *
 * For example, the pair [0, 1], indicates that to take course 0 you have to
 * first take course 1.
 *
 *
 * Return true if you can finish all courses. Otherwise, return false.
 *
 *
 * Example 1:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0]]
 * Output: true
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0. So it is possible.
 *
 *
 * Example 2:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
 * Output: false
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0, and to take course 0 you
 * should also have finished course 1. So it is impossible.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= numCourses <= 2000
 * 0 <= prerequisites.length <= 5000
 * prerequisites[i].length == 2
 * 0 <= ai, bi < numCourses
 * All the pairs prerequisites[i] are unique.
 *
 *
 */

/**
 * TimeComplexity : O(N + E)
 */
// @lc code=start
class Solution {

  public boolean canFinish(int numCourses, int[][] prerequisites) {
    ArrayList<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) {
      adj.add(new ArrayList<>());
    }
    int[] in = new int[numCourses];
    for (int i = 0; i < prerequisites.length; i++) {
      in[prerequisites[i][0]]++;
      adj.get(prerequisites[i][1]).add(prerequisites[i][0]);
    }
    Queue<Integer> queue = new LinkedList<Integer>();
    for (int i = 0; i < in.length; i++) {
      if (in[i] == 0) {
        queue.add(i);
      }
    }
    while (!queue.isEmpty()) {
      int vertex = queue.remove();
      for (var v : adj.get(vertex)) {
        if (--in[v] == 0) {
          queue.add(v);
        }
      }
    }
    for (int i = 0; i < in.length; i++) {
      if (in[i] != 0) {
        return false;
      }
    }
    return true;
  }
}
// @lc code=end
