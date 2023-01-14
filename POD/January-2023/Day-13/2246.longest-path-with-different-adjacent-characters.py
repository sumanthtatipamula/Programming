#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
#
# algorithms
# Hard (45.21%)
# Likes:    731
# Dislikes: 20
# Total Accepted:    17.8K
# Total Submissions: 37.6K
# Testcase Example:  '[-1,0,0,1,1,2]\n"abacbe"'
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
# represented by a 0-indexed array parent of size n, where parent[i] is the
# parent of node i. Since node 0 is the root, parent[0] == -1.
# 
# You are also given a string s of length n, where s[i] is the character
# assigned to node i.
# 
# Return the length of the longest path in the tree such that no pair of
# adjacent nodes on the path have the same character assigned to them.
# 
# 
# Example 1:
# 
# 
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters in the tree is the path: 0 -> 1 -> 3. The length of this path is
# 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the
# conditions. 
# 
# 
# Example 2:
# 
# 
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is
# returned.
# 
# 
# 
# Constraints:
# 
# 
# n == parent.length == s.length
# 1 <= n <= 10^5
# 0 <= parent[i] <= n - 1 for all i >= 1
# parent[0] == -1
# parent represents a valid tree.
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        for index, value in enumerate(parent):
            if(value != -1):
                adj[value] += [index]
        self.longest_path = 0
        def dfs(source):
            max1, max2 = 0,0
            for vertex in adj[source]:
                length = dfs(vertex)
                if(s[vertex] != s[source]):
                    if(length >= max1):
                        max2 = max1
                        max1 = length
                    elif(length > max2):
                        max2 = length
            self.longest_path = max(self.longest_path, max1 + max2 + 1)
            return max1 + 1
        dfs(0)
        return self.longest_path

        
# @lc code=end

