#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.17%)
# Likes:    13672
# Dislikes: 806
# Total Accepted:    1.5M
# Total Submissions: 4.8M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        def maxPalin(l, r):
            while(l > -1 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1 : r]
        for i in range(len(s)):
            palindrome = maxPalin(i - 1, i + 1)
            if(len(palindrome) > len(longestPalindrome)):
                longestPalindrome = palindrome
        for i in range(len(s) - 1):
            if(s[i] == s[i + 1]):
                palindrome = maxPalin(i - 1, i + 2)
                if(len(palindrome) > len(longestPalindrome)):
                    longestPalindrome = palindrome
        return longestPalindrome
        
# @lc code=end

