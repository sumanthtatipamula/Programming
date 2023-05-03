#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (33.68%)
# Total Accepted:    240.7K
# Total Submissions: 711.9K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# 
# Example 1:
# 
# 
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: s = "ab"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase English letters only.
# 
# 
#
class Solution(object):
    def minCut(self, s):
        mem = {}
        def generate(index):
            if(index == len(s)):
                return 0
            string = ''
            if(index in mem):
                return mem[index]
            count = float("Inf")
            for i in range(index, len(s)):
                string += s[i]
                if(string == string[::- 1]):
                    count = min(count, generate(i + 1))
            mem[index] = count + 1
            return mem[index]
        return generate(0) - 1
