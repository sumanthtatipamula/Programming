#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#
# https://leetcode.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (57.61%)
# Total Accepted:    96.4K
# Total Submissions: 167.4K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# 
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# 
# Example 1:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# 
# Example 2:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# 
# 
#
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root, rank, rootToElementsMap, result = [i for i in range(len(s))], [0] * len(s), {}, ""
        def find(x):
            if(root[x] == x):
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if(rootX != rootY):
                if(rank[rootX] > rank[rootY]):
                    root[rootY] = rootX
                elif(rank[rootY] > rank[rootX]):
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
        for u,v in pairs:
            union(u, v)
        for i in range(len(s)):
            rootE = find(i)
            if(rootE not in rootToElementsMap):
                rootToElementsMap[rootE] = [0, []]
            rootToElementsMap[rootE][-1].append(s[i])
        for key in rootToElementsMap.keys():
            rootToElementsMap[key][-1].sort()
        for i in range(len(s)):
            rootE = find(i)
            index, elements = rootToElementsMap[rootE]
            result += elements[index]
            rootToElementsMap[rootE][0] += 1
        return result
        
