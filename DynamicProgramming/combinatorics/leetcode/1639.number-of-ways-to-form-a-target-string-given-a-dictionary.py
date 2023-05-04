#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
#
# algorithms
# Hard (43.11%)
# Total Accepted:    48.2K
# Total Submissions: 89.3K
# Testcase Example:  '["acca","bbbb","caca"]\n"aba"'
#
# You are given a list of strings of the same length words and a string
# target.
# 
# Your task is to form target using the given words under the following
# rules:
# 
# 
# target should be formed from left to right.
# To form the i^th character (0-indexed) of target, you can choose the k^th
# character of the j^th string in words if target[i] = words[j][k].
# Once you use the k^th character of the j^th string of words, you can no
# longer use the x^th character of any string in words where x <= k. In other
# words, all characters to the left of or at index k become unusuable for every
# string.
# Repeat the process until you form the string target.
# 
# 
# Notice that you can use multiple characters from the same string in words
# provided the conditions above are met.
# 
# Return the number of ways to form target from words. Since the answer may be
# too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
# 
# 
# Example 2:
# 
# 
# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# All strings in words have the same length.
# 1 <= target.length <= 1000
# words[i] and target contain only lowercase English letters.
# 
# 
#
from collections import defaultdict
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        freq = defaultdict(lambda: defaultdict(lambda: 0))
        max_index = 0
        for word in words:
          for index, char in enumerate(word):
             max_index = max(max_index, index)
             freq[index][char] += 1
        mem = {}
        def ways_to_built_target(freqIndex, index):
            if(index == len(target)):
               return 1
            if((max_index - freqIndex + 1) < (len(target) - index)):
               return 0
            if((freqIndex, index) in mem):
               return mem[(freqIndex, index)]
            ways = ways_to_built_target(freqIndex + 1, index)
            if(freq[freqIndex][target[index]] > 0):
                ways = (ways + freq[freqIndex][target[index]] * ways_to_built_target(freqIndex + 1, index + 1)) % mod
            mem[(freqIndex, index)] = ways
            return ways
        return ways_to_built_target(0, 0)

