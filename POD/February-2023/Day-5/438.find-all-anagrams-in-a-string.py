#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (49.05%)
# Likes:    9683
# Dislikes: 295
# Total Accepted:    670.4K
# Total Submissions: 1.4M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# 
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        lettersmap = dict.fromkeys(string.ascii_lowercase, 0)
        for letter in p:
            lettersmap[letter] += 1
        count  = 0
        for i in range(len(s)):
            lettersmap[s[i]] -= 1
            if(lettersmap[s[i]] >= 0):
                count += 1
            if(count == len(p)):
                result.append(i - len(p) + 1)
            if(i >= len(p) - 1):
                lettersmap[s[i - len(p) + 1]] += 1
                if(lettersmap[s[i - len(p) + 1]] > 0):
                    count -= 1
        return result
        
# @lc code=end

