#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (62.88%)
# Total Accepted:    637.7K
# Total Submissions: 981.4K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        mem = {}
        def generate(index):
            if(index == len(s)):
                return [[]]
            string = ''
            new_sublist = []
            if(index in mem):
                return mem[index]
            for i in range(index, len(s)):
                string += s[i]
                if(string == string[::- 1]):
                    sub_list = generate(i + 1)
                    for array in sub_list:
                        new_sublist.append([string] + array)
            mem[index] = new_sublist
            return mem[index]
        return generate(0)


        
