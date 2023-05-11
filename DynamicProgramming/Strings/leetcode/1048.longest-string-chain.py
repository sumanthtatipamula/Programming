#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (59.16%)
# Total Accepted:    306.4K
# Total Submissions: 517K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# You are given an array of words where each word consists of lowercase English
# letters.
# 
# wordA is a predecessor of wordB if and only if we can insert exactly one
# letter anywhere in wordA without changing the order of the other characters
# to make it equal to wordB.
# 
# 
# For example, "abc" is a predecessor of "abac", while "cba" is not a
# predecessor of "bcad".
# 
# 
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
# where word1 is a predecessor of word2, word2 is a predecessor of word3, and
# so on. A single word is trivially a word chain with k == 1.
# 
# Return the length of the longest possible word chain with words chosen from
# the given list of words.
# 
# 
# Example 1:
# 
# 
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# 
# 
# Example 2:
# 
# 
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc",
# "pcxbc", "pcxbcf"].
# 
# 
# Example 3:
# 
# 
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word
# chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the
# letters is changed.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.
# 
# 
#
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        mem = {}
        def longest_chain(word):
            if(len(word) == 0 or word not in words):
                return 0
            if(word in mem):
                return mem[word]
            result = 0
            for i in range(0, len(word)):
                result =  max(result, 1 + longest_chain(word[0: i] + word[i + 1:]))
            mem[word] =  result
            return result
        result = 0
        for word in words:
            result = max(result, longest_chain(word))
        return result

    def longestStrChain(self, words: List[str]) -> int:
        mem = defaultdict(int)
        words.sort(key = lambda x: len(x))
        max_length = 0
        for word in words:
            result = 1
            for i in range(0, len(word)):
                predecessor = word[0: i] + word[i + 1:]
                if(predecessor in words):
                    result = max(result, 1 + mem[predecessor])
            mem[word] = result
            max_length = max(max_length, result)
        return max_length

