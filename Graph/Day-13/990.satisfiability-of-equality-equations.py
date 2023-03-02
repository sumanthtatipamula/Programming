#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (50.75%)
# Total Accepted:    108.7K
# Total Submissions: 215K
# Testcase Example:  '["a==b","b!=a"]'
#
# You are given an array of strings equations that represent relationships
# between variables where each string equations[i] is of length 4 and takes one
# of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
# letters (not necessarily different) that represent one-letter variable
# names.
# 
# Return true if it is possible to assign integers to variable names so as to
# satisfy all the given equations, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
# 
# 
# Example 2:
# 
# 
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.
# 
# 
#
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = [i for i in range(26)]
        rank = [0 for _ in range(26)]
        def find(x):
            if(root[x] == x):
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):  
            if(x == y):
                return   
            if(rank[x] > rank[y]):
                root[y] = x
            elif(rank[x] < rank[y]):
                root[x] = y
            else:
                root[y] = x
                rank[x] += 1
        def getIndex(a):
            return ord(a) - ord('a')

        for equation in equations:
            a, eq, b = getIndex(equation[0]), equation[1] == '=',getIndex(equation[-1])
            if(eq and a != b):
                union(find(a), find(b))
        for equation in equations:
            a, eq, b = getIndex(equation[0]), equation[1] == '=',getIndex(equation[-1])
            if(not eq and (a == b or find(a) == find(b))):
                    return False
        return True
        
