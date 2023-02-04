#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.52%)
# Total Accepted:    547.5K
# Total Submissions: 1.3M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)
        if(s1_length == 0):
            return True
        letters = dict.fromkeys(string.ascii_lowercase, 0)
        for letter in s1:
            letters[letter] += 1
        count = 0
        for i in range(0, len(s2)):
            letters[s2[i]] -= 1
            if(letters[s2[i]] >= 0):
                count += 1
            if(count == s1_length):
                return True
            if(i >= s1_length - 1):
                if(letters[s2[i - (s1_length - 1)]] >= 0):
                    count -= 1
                letters[s2[i - (s1_length - 1)]] += 1
        return False
        
